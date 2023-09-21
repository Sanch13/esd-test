from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str
    DEBUG: bool
    ALLOWED_HOSTS: str

    ENGINE: str
    NAME_DB: str
    USER: str
    PASSWORD: str
    HOST: str
    PORT: str

    EMAIL_HOST: str
    EMAIL_PORT: int
    DEFAULT_FROM_EMAIL: str
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_TLS: bool
    EMAIL_USE_SSL: bool

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()
