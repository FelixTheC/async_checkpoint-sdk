from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class MdsRequestEdit(BaseModel):
    ipv6_address: str = Field(
        alias="ipv6-address", description="""IPv6 Address. requires manual restart."""
    )
    hardware: str = Field(
        alias="hardware",
        description="""Hardware name. For example: Open server, Smart-1, Other.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    os: str = Field(
        alias="os",
        description="""Operating system name. For example: Gaia, Linux, SecurePlatform.""",
    )
    version: str = Field(alias="version", description="""System version.""")
    one_time_password: str = Field(
        alias="one-time-password",
        description="""Secure internal connection one time password.""",
    )
    ip_pool_first: str = Field(
        alias="ip-pool-first", description="""First IP address in the range."""
    )
    ip_pool_last: str = Field(alias="ip-pool-last", description="""Last IP address in the range.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
