from pydantic import BaseModel, Field


class MdsRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    ip_address: str = Field(alias="ip-address", description="""IPv4 address.""")
    hardware: str = Field(
        alias="hardware", description="""Hardware name. For example: Open server, Smart-1, Other."""
    )
    os: str = Field(
        alias="os",
        description="""Operating system name. For example: Gaia, Linux, SecurePlatform.""",
    )
    version: str = Field(alias="version", description="""System version.""")
    one_time_password: str = Field(
        alias="one-time-password", description="""Secure internal connection one time password."""
    )
    server_type: str = Field(alias="server-type", description="""Type of the management server.""")
    ip_pool_first: str = Field(
        alias="ip-pool-first", description="""First IP address in the range."""
    )
    ip_pool_last: str = Field(alias="ip-pool-last", description="""Last IP address in the range.""")
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
