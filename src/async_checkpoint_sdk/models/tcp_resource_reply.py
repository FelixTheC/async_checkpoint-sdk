from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .object import Object
from .pydantic import BaseModel, Field
from .tcp_resource_cvp_reply import TcpResourceCvpReply
from .ufp_object_reply import UfpObjectReply


class TcpResourceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    resource_type: str = Field(
        alias="resource-type", description="""The type of the TCP resource."""
    )
    exception_track: Object = Field(
        alias="exception-track",
        description="""Configures how to track connections that match this rule but fail the content security checks. An example of an exception is a connection with an unsupported scheme or method.""",
    )
    ufp_settings: UfpObjectReply = Field(alias="ufp-settings", description="""UFP settings.""")
    cvp_settings: TcpResourceCvpReply = Field(alias="cvp-settings", description="""CVP settings.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
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
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
