from pydantic import BaseModel, Field


class ProtectionRequestShow(BaseModel):
    show_capture_packets_and_track: bool = Field(
        alias="show-capture-packets-and-track",
        description="""Indicates whether to calculate and show Capture Packets And Track field in reply.""",
    )
    show_ips_additional_properties: bool = Field(
        alias="show-ips-additional-properties",
        description="""Indicates whether to calculate and show ips additional properties field in reply.""",
    )
    show_profiles: bool = Field(
        alias="show-profiles",
        description="""Indicates whether to calculate and show profiles field in reply.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
