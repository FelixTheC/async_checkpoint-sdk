from api_date_reply import ApiDateReply
from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class GlobalAssignmentReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    assignment_status: str = Field(alias="assignment-status", description="""N/A""")
    assignment_up_to_date: ApiDateReply = Field(
        alias="assignment-up-to-date", description="""The time when the assignment was assigned."""
    )
    dependent_domain: ApiObjectStandardIdentifier = Field(
        alias="dependent-domain",
        description="""Dependent domain. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    global_access_policy: str = Field(
        alias="global-access-policy",
        description="""Global domain access policy that is assigned to a dependent domain.""",
    )
    global_domain: ApiObjectStandardIdentifier = Field(
        alias="global-domain",
        description="""Global domain. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    global_threat_prevention_policy: str = Field(
        alias="global-threat-prevention-policy",
        description="""Global domain threat prevention policy that is assigned to a dependent domain.""",
    )
    manage_protection_actions: bool = Field(
        alias="manage-protection-actions", description="""N/A"""
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
