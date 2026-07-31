from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from if_map_server_authentication_reply import IfMapServerAuthenticationReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from object import Object
from pydantic import BaseModel, Field


class IfMapReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    port: int = Field(alias="port", description="""IF-MAP server port number.""")
    version: str = Field(alias="version", description="""IF-MAP version.""")
    host: Object = Field(
        alias="host",
        description="""Host that is IF-MAP server. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    path: str = Field(alias="path", description="""N/A""")
    monitored_ips: list[dict] = Field(
        alias="monitored-ips", description="""IP ranges to be monitored by the IF-MAP client."""
    )
    query_whole_ranges: bool = Field(
        alias="query-whole-ranges",
        description="""Indicate whether to query whole ranges instead of single IP.""",
    )
    authentication: IfMapServerAuthenticationReply = Field(
        alias="authentication",
        description="""Authentication configuration for the IF-MAP server.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
