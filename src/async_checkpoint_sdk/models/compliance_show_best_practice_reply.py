from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from compliance_user_defined_firewall_reply import ComplianceUserDefinedFirewallReply
from compliance_user_defined_gaia_os_reply import ComplianceUserDefinedGaiaOsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field
from show_best_practice_relevant_objects_reply import ShowBestPracticeRelevantObjectsReply


class ComplianceShowBestPracticeReply(BaseModel):
    name: str = Field(alias="name", description="""The Best Practice name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""The type of Best Practice.""")
    action_item: str = Field(
        alias="action-item",
        description="""Required action item to comply with the Best Practice.""",
    )
    active: bool = Field(alias="active", description="""Shows if the Best Practice is active.""")
    best_practice_id: str = Field(
        alias="best-practice-id", description="""ID of the Best Practice."""
    )
    blade: str = Field(
        alias="blade", description="""The Software Blade name of the Best Practice."""
    )
    description: str = Field(
        alias="description", description="""Description of the Best Practice."""
    )
    due_date: str = Field(
        alias="due-date",
        description="""Shows if there is a due date for the action item of this Best Practice.""",
    )
    regulations: list[dict] = Field(
        alias="regulations",
        description="""The applicable regulations of the Best Practice. Appears only when the value of the 'show-regulations' parameter is set to 'true'.""",
    )
    relevant_objects: ShowBestPracticeRelevantObjectsReply = Field(
        alias="relevant-objects", description="""The applicable objects of the Best Practice."""
    )
    status: str = Field(alias="status", description="""The current status of the Best Practice.""")
    user_defined: bool = Field(
        alias="user-defined",
        description="""Shows if the Best Practice is a user-defined Best Practice.""",
    )
    user_defined_firewall: ComplianceUserDefinedFirewallReply = Field(
        alias="user-defined-firewall",
        description="""The definitions of the user-defined Firewall Best Practice. Relevant only for Firewall Best Practices created by the user.""",
    )
    user_defined_gaia_os: ComplianceUserDefinedGaiaOsReply = Field(
        alias="user-defined-gaia-os",
        description="""The definitions of the user-defined Gaia OS Best Practice. Relevant only for Gaia OS Best Practices created by the user.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
