from pydantic import BaseModel, Field


class SupportedFirmwarePlatforms(BaseModel):
    default: str = Field(alias="default", description="""Default gateway firmware platform.""")
    firmwareplatforms: list[str] = Field(
        alias="firmwarePlatforms", description="""List of gateway firmware platforms."""
    )
