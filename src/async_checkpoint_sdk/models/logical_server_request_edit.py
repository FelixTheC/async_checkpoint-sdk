from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class LogicalServerRequestEdit(BaseModel):
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    server_group: str = Field(
        alias="server-group",
        description="""Server group associated with the logical server. 
Identified by name or UID.""",
    )
    server_type: str = Field(
        alias="server-type", description="""Type of server for the logical server."""
    )
    persistence_mode: bool = Field(
        alias="persistence-mode",
        description="""Indicates if persistence mode is enabled for the logical server.""",
    )
    persistency_type: str = Field(
        alias="persistency-type",
        description="""Persistency type for the logical server.""",
    )
    balance_method: str = Field(
        alias="balance-method",
        description="""Load balancing method for the logical server.""",
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
