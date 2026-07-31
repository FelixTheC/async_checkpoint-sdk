from pydantic import BaseModel, Field


class SupportedVersions(BaseModel):
    default: str = Field(alias="default", description="""Default gateway platform version.""")
    versions: list[str] = Field(
        alias="versions", description="""List of gateway platform versions."""
    )
