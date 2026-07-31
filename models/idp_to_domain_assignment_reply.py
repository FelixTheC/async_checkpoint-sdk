from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from object import Object
from pydantic import BaseModel, Field


class IdpToDomainAssignmentReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    assigned_domain: Object = Field(
        alias="assigned-domain",
        description="""Represents the Domain assigned by 'idp-to-domain-assignment'.""",
    )
    identity_provider: Object = Field(
        alias="identity-provider",
        description="""Represents the Identity Provider to be used for login. If 'using-default' value is 'true' show the Identity Provider used by 'idp-default-assignment'.""",
    )
    identity_provider_set: bool = Field(
        alias="identity-provider-set",
        description="""True if 'identity-provider' value is set.""",
    )
    using_default: bool = Field(
        alias="using-default",
        description="""Is this assignment override by 'idp-default-assignment'.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
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
