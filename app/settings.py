from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Database connections (required)
    GRAPH_DB_URI: str = Field(..., alias="GRAPH_DB_URI")
    GRAPH_DB_USER: str = Field(..., alias="GRAPH_DB_USER")
    GRAPH_DB_PASSWORD: str = Field(..., alias="GRAPH_DB_PASSWORD")
    VULN_DB_URI: str = Field(..., alias="VULN_DB_URI")
    POSTGRES_HOST: str = Field(..., alias="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(..., alias="POSTGRES_PORT")
    POSTGRES_DB: str = Field(..., alias="POSTGRES_DB")
    POSTGRES_USER: str = Field(..., alias="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field(..., alias="POSTGRES_PASSWORD")

    # Application settings (safe defaults)
    DOCS_URL: str | None = Field(None, alias="DOCS_URL")
    SERVICES_ALLOWED_ORIGINS: list[str] = Field(["*"], alias="SERVICES_ALLOWED_ORIGINS")

    # Database Configuration
    DB_MIN_POOL_SIZE: int = 10
    DB_MAX_POOL_SIZE: int = 100
    DB_MAX_IDLE_TIME_MS: int = 60000
    DB_DEFAULT_QUERY_TIMEOUT_MS: int = 30000


@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore[call-arg]


settings: Settings = get_settings()
