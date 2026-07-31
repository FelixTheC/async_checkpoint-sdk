from .pydantic import BaseModel, Field


class GatewayCkpRequestShow(BaseModel):
    show_portals_certificate: bool = Field(
        alias="show-portals-certificate",
        description="""Indicates whether to show the portals certificate value in the reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    show_advanced_settings: bool = Field(
        alias="show-advanced-settings",
        description="""Indicates whether to calculate and show advanced settings in reply, e.g. SAM.""",
    )
