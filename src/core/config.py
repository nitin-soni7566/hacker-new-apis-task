from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    HACKER_NEWS_API_URL: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_PASSWORD: str
    REDIS_EXP_TIME: int

    model_config = SettingsConfigDict(
        env_file=".env", extra="ignore", env_file_encoding="utf-8"
    )


settings = Settings()
