import json
from pathlib import Path
from typing import Dict, Optional

# Default locale
DEFAULT_LOCALE = "en"

# Supported locales
SUPPORTED_LOCALES = ["en", "cn", "vi"]

# Translation cache
_translations: Dict[str, Dict] = {}


def _load_translations() -> Dict[str, Dict]:
    """Load all translation files"""
    global _translations
    
    if _translations:
        return _translations
    
    translations = {}
    messages_dir = Path(__file__).parent / "messages"
    
    for locale in SUPPORTED_LOCALES:
        translation_file = messages_dir / f"{locale}.json"
        if translation_file.exists():
            with open(translation_file, "r", encoding="utf-8") as f:
                translations[locale] = json.load(f)
    
    _translations = translations
    return translations


def _get_nested_value(data: dict, key_path: str, default: Optional[str] = None) -> Optional[str]:
    """Get nested value from dict using dot notation (e.g., 'api.depts.list_summary')"""
    keys = key_path.split(".")
    value = data
    
    for key in keys:
        if isinstance(value, dict):
            value = value.get(key)
            if value is None:
                return default
        else:
            return default
    
    return value if isinstance(value, str) else default


def t(key: str, locale: str = DEFAULT_LOCALE) -> str:
    """
    Translate a key to the specified locale.
    
    Args:
        key: Translation key in dot notation (e.g., 'api.depts.list_summary')
        locale: Language code (default: 'en')
    
    Returns:
        Translated string or the key if translation not found
    """
    translations = _load_translations()
    
    # Use default locale if requested locale not available
    if locale not in translations:
        locale = DEFAULT_LOCALE
    
    # Try to get translation
    translation = _get_nested_value(translations.get(locale, {}), key)
    
    # Fallback to default locale if not found
    if translation is None and locale != DEFAULT_LOCALE:
        translation = _get_nested_value(translations.get(DEFAULT_LOCALE, {}), key)
    
    # Return key itself if no translation found
    return translation if translation else key


def get_locale_from_header(accept_language: Optional[str] = None) -> str:
    """
    Extract locale from Accept-Language header.
    
    Args:
        accept_language: Accept-Language header value (e.g., 'en-US,en;q=0.9,vi;q=0.8')
    
    Returns:
        Supported locale code or default locale
    """
    if not accept_language:
        return DEFAULT_LOCALE
    
    # Parse Accept-Language header
    languages = []
    for lang in accept_language.split(","):
        lang = lang.strip().split(";")[0].split("-")[0].lower()
        languages.append(lang)
    
    # Find first supported locale
    for lang in languages:
        if lang in SUPPORTED_LOCALES:
            return lang
    
    return DEFAULT_LOCALE

