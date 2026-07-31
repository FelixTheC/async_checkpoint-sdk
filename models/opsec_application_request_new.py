from cpmi_request import CpmiRequest
from lea_request import LeaRequest
from pydantic import BaseModel, Field


class OpsecApplicationRequestNew(BaseModel):
    cpmi: CpmiRequest = Field(
        alias="cpmi", description="""Used to setup the CPMI client entity."""
    )
    lea: LeaRequest = Field(
        alias="lea", description="""Used to setup the LEA client entity."""
    )
    one_time_password: str = Field(
        alias="one-time-password",
        description="""A password required for establishing a Secure Internal Communication (SIC).""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
