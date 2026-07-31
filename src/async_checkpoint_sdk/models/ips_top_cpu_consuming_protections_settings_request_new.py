from .pydantic import BaseModel, Field


class IpsTopCpuConsumingProtectionsSettingsRequestNew(BaseModel):
    disable_period: int = Field(
        alias="disable-period",
        description="""Duration (in hours) for disabling the protections.""",
    )
    disable_under_load: bool = Field(
        alias="disable-under-load",
        description="""Temporarily disable/enable top CPU consuming IPS protections.""",
    )
