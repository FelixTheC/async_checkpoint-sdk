from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from i_p_service_reply import IPServiceReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from server_object_reply import ServerObjectReply


class TacacsReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    encryption: bool = Field(
        alias="encryption",
        description="""Is there a secret key defined on the server. Must be set true when server-type was selected to be TACACS+.""",
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    priority: int = Field(
        alias="priority",
        description="""The priority of the TACACS Server in case it is a member of a TACACS Group.""",
    )
    server: ServerObjectReply = Field(
        alias="server", description="""The UID or Name of the host that is the TACACS Server."""
    )
    server_type: str = Field(alias="server-type", description="""Server type, TACACS or TACACS+.""")
    service: IPServiceReply = Field(
        alias="service", description="""Server service, only relevant when server-type is TACACS."""
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
