from .add import add
from .if_map_monitored_ips_request import IfMapMonitoredIpsRequest
from .if_map_server_authentication_request import IfMapServerAuthenticationRequest
from .pydantic import BaseModel, Field
from .remove import remove
from .update import update


class IfMapRequestEdit(BaseModel):
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    port: int = Field(alias="port", description="""IF-MAP server port number.""")
    version: str = Field(alias="version", description="""IF-MAP version.""")
    host: str = Field(
        alias="host",
        description="""Host that is IF-MAP server. 
Identified by name or UID.""",
    )
    path: str = Field(alias="path", description="""N/A""")
    monitored_ips: add | remove | update | IfMapMonitoredIpsRequest | list[dict] = Field(
        alias="monitored-ips",
        description="""IP ranges to be monitored by the IF-MAP client.""",
    )
    query_whole_ranges: bool = Field(
        alias="query-whole-ranges",
        description="""Indicate whether to query whole ranges instead of single IP.""",
    )
    authentication: IfMapServerAuthenticationRequest = Field(
        alias="authentication",
        description="""Authentication configuration for the IF-MAP server.""",
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
