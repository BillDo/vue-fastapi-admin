import os
import typing

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    VERSION: str = "0.1.0"
    APP_TITLE: str = "Vue FastAPI Admin"
    PROJECT_NAME: str = "Vue FastAPI Admin"
    APP_DESCRIPTION: str = "Description"

    CORS_ORIGINS: typing.List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: typing.List = ["*"]
    CORS_ALLOW_HEADERS: typing.List = ["*"]

    DEBUG: bool = True

    PROJECT_ROOT: str = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    BASE_DIR: str = os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir))
    LOGS_ROOT: str = os.path.join(BASE_DIR, "app/logs")
    SECRET_KEY: str = "3488a63e1765035d386f05409663f55c83bfae3b3c61a932744b20ad14244dcf"  # openssl rand -hex 32
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 day

    # Database configuration - can be set via environment variables
    # Options: sqlite, mysql, postgres
    # Note: PostgreSQL is now the default
    # To use SQLite, set DB_TYPE=sqlite
    # To use MySQL, set DB_TYPE=mysql, DB_PORT=3306, DB_USER=root
    DB_TYPE: str = "postgres"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432  # PostgreSQL default port
    DB_USER: str = "postgres"  # PostgreSQL default user
    DB_PASSWORD: str = "admin"
    DB_NAME: str = "my_website"
    DB_FILE_PATH: str = f"{BASE_DIR}/db.sqlite3"

    @property
    def TORTOISE_ORM(self) -> dict:
        """Generate TORTOISE_ORM config based on DB_TYPE"""
        connections = {}
        default_connection = "postgres"
        
        if self.DB_TYPE == "mysql":
            connections["mysql"] = {
                "engine": "tortoise.backends.mysql",
                "credentials": {
                    "host": self.DB_HOST,
                    "port": self.DB_PORT,
                    "user": self.DB_USER,
                    "password": self.DB_PASSWORD,
                    "database": self.DB_NAME,
                },
            }
            default_connection = "mysql"
        elif self.DB_TYPE == "postgres":
            connections["postgres"] = {
                "engine": "tortoise.backends.asyncpg",
                "credentials": {
                    "host": self.DB_HOST,
                    "port": self.DB_PORT,
                    "user": self.DB_USER,
                    "password": self.DB_PASSWORD,
                    "database": self.DB_NAME,
                },
            }
            default_connection = "postgres"
        else:  # sqlite (fallback)
            connections["sqlite"] = {
                "engine": "tortoise.backends.sqlite",
                "credentials": {"file_path": self.DB_FILE_PATH},
            }
            default_connection = "sqlite"

        return {
            "connections": connections,
            "apps": {
                "models": {
                    "models": ["app.models", "aerich.models"],
                    "default_connection": default_connection,
                },
            },
            "use_tz": False,  # Whether to use timezone-aware datetimes
            "timezone": "Asia/Shanghai",  # Timezone setting
        }

    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


settings = Settings()
