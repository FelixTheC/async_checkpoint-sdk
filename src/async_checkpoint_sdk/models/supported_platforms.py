from pydantic import BaseModel, Field


class SupportedPlatforms(BaseModel):
    default: str = Field(alias="default", description="""Default platform.""")
    platforms: list[str] = Field(
        alias="platforms", description="""List of Check Point gateway platforms."""
    )
