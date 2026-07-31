from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class AccessLayerReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    applications_and_url_filtering: bool = Field(
        alias="applications-and-url-filtering",
        description="""Whether Applications & URL Filtering blade is enabled on this layer.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness",
        description="""Whether Content Awareness blade is enabled on this layer.""",
    )
    detect_using_x_forward_for: bool = Field(
        alias="detect-using-x-forward-for",
        description="""Whether X-Forward-For HTTP header is been used.""",
    )
    dynamic_layer: bool = Field(
        alias="dynamic-layer",
        description="""Whether this layer is set as a Dynamic layer.""",
    )
    firewall: bool = Field(
        alias="firewall",
        description="""Whether Firewall blade is enabled on this layer.""",
    )
    implicit_cleanup_action: str = Field(
        alias="implicit-cleanup-action",
        description="""The default catch-all action for traffic that does not match any explicit or implied rules in the layer.""",
    )
    mobile_access: bool = Field(
        alias="mobile-access",
        description="""Whether Mobile Access blade is enabled on this layer.""",
    )
    parent_layer: str = Field(
        alias="parent-layer", description="""Parent layer of this layer."""
    )
    shared: bool = Field(
        alias="shared", description="""Whether this layer is shared."""
    )
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
