<template>
  <n-dropdown :options="options" @select="handleChangeLocale">
    <div class="language-switcher">
      {{ currentLocaleText }}
      <IconMdiChevronDown class="icon" />
    </div>
  </n-dropdown>
</template>

<script setup>
import { computed } from 'vue'
import { useI18n } from 'vue-i18n'
import { NDropdown } from 'naive-ui'
import IconMdiChevronDown from '~icons/mdi/chevron-down'

const { locale, t } = useI18n()

const currentLocaleText = computed(() => {
  const localeMap = {
    en: 'EN',
    cn: '中文',
    vi: 'Tiếng Việt',
  }
  return localeMap[locale.value] || 'EN'
})

const options = computed(() => [
  {
    label: 'EN',
    key: 'en',
  },
  {
    label: '中文',
    key: 'cn',
  },
  {
    label: 'Tiếng Việt',
    key: 'vi',
  },
])

const handleChangeLocale = (value) => {
  locale.value = value
  localStorage.setItem('locale', value)
}
</script>

<style scoped lang="scss">
.language-switcher {
  display: flex;
  align-items: center;
  gap: 4px;
  cursor: pointer;
  padding: 4px 8px;
  border-radius: 4px;
  transition: background-color 0.3s;

  &:hover {
    background-color: rgba(0, 0, 0, 0.05);
  }

  .icon {
    font-size: 16px;
  }
}
</style>

