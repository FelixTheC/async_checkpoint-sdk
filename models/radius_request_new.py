from object import Object
from pydantic import BaseModel, Field
from radius_accounting_object_request import RadiusAccountingObjectRequest


class RadiusRequestNew(BaseModel):
    service: str = Field(
        alias="service",
        description="""The UID or Name of the Service to which the RADIUS server listens.""",
    )
    version: str = Field(
        alias="version",
        description="""The version can be either RADIUS Version 1.0, which is RFC 2138 compliant, and RADIUS Version 2.0 which is RFC 2865 compliant.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""The type of authentication protocol that will be used when authenticating the user to the RADIUS server.""",
    )
    priority: int = Field(
        alias="priority",
        description="""The priority of the RADIUS Server in case it is a member of a RADIUS Group.""",
    )
    accounting: RadiusAccountingObjectRequest = Field(
        alias="accounting", description="""Accounting settings."""
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
    groups: Object = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
