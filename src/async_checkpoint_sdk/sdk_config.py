import tomllib
from pathlib import Path

from pydantic import BaseModel, Field


class SDKConfig(BaseModel):
    server: str
    port: int
    username: str
    password: str = Field(default="")
    api_key: str = Field(default="", alias="api-key")

    @classmethod
    def load_from_toml(cls, file: Path) -> SDKConfig:
        with file.open("rb") as fp:
            data = tomllib.load(fp)

        return cls(**data["checkpoint"]["config"])
