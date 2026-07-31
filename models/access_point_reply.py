from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class AccessPointReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    apn: str = Field(alias="apn", description="""APN name.""")
    block_traffic_other_end_user_domains: bool = Field(
        alias="block-traffic-other-end-user-domains",
        description="""Block MS to MS traffic between this and other APN end user domains enabled.""",
    )
    block_traffic_this_end_user_domain: bool = Field(
        alias="block-traffic-this-end-user-domain",
        description="""Block MS to MS traffic within this end user domain enabled.""",
    )
    end_user_domain: ApiObjectStandardIdentifier = Field(
        alias="end-user-domain",
        description="""End user domain identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    enforce_end_user_domain: bool = Field(
        alias="enforce-end-user-domain",
        description="""Enforce end user domain enabled.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
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
