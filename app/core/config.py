from __future__ import annotations

from pathlib import Path
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ── Database ──────────────────────────────────────────────
    database_url: str = "postgresql+psycopg://dils:dils@localhost:5432/dils"

    # ── Security ──────────────────────────────────────────────
    secret_key: str = "change-me-to-random-64-chars"
    session_timeout_minutes: int = 480

    # ── Locks ─────────────────────────────────────────────────
    lock_timeout_seconds: int = 180
    lock_heartbeat_seconds: int = 30

    # ── App ───────────────────────────────────────────────────
    debug: bool = True
    log_level: str = "INFO"
    host: str = "127.0.0.1"
    port: int = 8000

    # ── Paths ─────────────────────────────────────────────────
    @property
    def base_dir(self) -> Path:
        return BASE_DIR

    @property
    def templates_dir(self) -> Path:
        return BASE_DIR / "templates"

    @property
    def static_dir(self) -> Path:
        return BASE_DIR / "static"

    @property
    def logs_dir(self) -> Path:
        return BASE_DIR / "logs"

    @property
    def backups_dir(self) -> Path:
        return BASE_DIR / "backups"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
