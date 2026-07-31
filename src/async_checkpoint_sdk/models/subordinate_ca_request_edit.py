from .add import add
from .automatic_enrollment_request import AutomaticEnrollmentRequest
from .object import Object
from .pydantic import BaseModel, Field
from .remove import remove


class SubordinateCaRequestEdit(BaseModel):
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    automatic_enrollment: AutomaticEnrollmentRequest = Field(
        alias="automatic-enrollment",
        description="""Certificate automatic enrollment.""",
    )
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    groups: Object = Field(alias="groups", description="""Collection of group identifiers.""")
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
