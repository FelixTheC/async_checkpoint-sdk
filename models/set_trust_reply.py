from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from trust_details_reply import TrustDetailsReply


class SetTrustReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    auto_generate_ip: bool = Field(
        alias="auto-generate-ip",
        description="""Use an automatically generated IP address for the Gateway object (applies only to Smart-1 Cloud).""",
    )
    sic_message: str = Field(
        alias="sic-message", description="""Secure Internal Communication message."""
    )
    sic_name: str = Field(
        alias="sic-name", description="""Secure Internal Communication name."""
    )
    sic_state: str = Field(
        alias="sic-state", description="""Secure Internal Communication state."""
    )
    trust_details: TrustDetailsReply = Field(
        alias="trust-details", description="""Details for trusted communication."""
    )
    trust_method: str = Field(
        alias="trust-method",
        description="""Trust method that was used for establishing communication.""",
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
