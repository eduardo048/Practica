import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Settings:
    app_name: str
    data_file: Path


@lru_cache
def get_settings() -> Settings:
    data_file = Path(os.getenv("DATA_FILE", BASE_DIR / "data" / "sales.csv"))

    if not data_file.is_absolute():
        data_file = BASE_DIR / data_file

    return Settings(
        app_name=os.getenv("APP_NAME", "Practica API"),
        data_file=data_file,
    )

