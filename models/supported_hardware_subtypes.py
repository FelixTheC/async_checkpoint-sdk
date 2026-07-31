from pydantic import BaseModel, Field


class SupportedHardwareSubtypes(BaseModel):
    default: str = Field(alias="default", description="""Default hardware subtype.""")
    hardware_subtypes: list[str] = Field(
        alias="hardware-subtypes",
        description="""List of Check Point hardware subtypes.""",
    )
