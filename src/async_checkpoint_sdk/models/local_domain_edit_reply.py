from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class LocalDomainEditReply(BaseModel):
    tasks: list[dict] = Field(
        alias="tasks",
        description="""Asynchronous task unique identifiers. This field is an alternative to all the fields presented below and is populated if 'set-domain' command was executed asynchronously. This happens when 'servers' field was provided in the request.""",
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    type: str = Field(alias="type", description="""Object type.""")
    domain_type: str = Field(alias="domain-type", description="""N/A""")
    global_domain_assignments: list[dict] = Field(
        alias="global-domain-assignments", description="""N/A"""
    )
    servers: list[dict] = Field(alias="servers", description="""Domain servers.""")
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
