from pydantic import BaseModel, Field


class SupportedHardware(BaseModel):
    default: str = Field(alias="default", description="""Default hardware.""")
    hardware: list[str] = Field(alias="hardware", description="""List of Check Point hardware.""")
