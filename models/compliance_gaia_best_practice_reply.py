from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class ComplianceGaiaBestPracticeReply(BaseModel):
    name: str = Field(alias="name", description="""The Best Practice name.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""The type of Best Practice.""")
    action_item: str = Field(
        alias="action-item",
        description="""Required action item to comply with the Best Practice.""",
    )
    best_practice_id: str = Field(
        alias="best-practice-id", description="""ID of the Best Practice."""
    )
    description: str = Field(
        alias="description", description="""Description of the Best Practice."""
    )
    expected_output_base64: str = Field(
        alias="expected-output-base64",
        description="""The expected output of the script in Base64. Available only for user-defined best practices.""",
    )
    practice_script_base64: str = Field(
        alias="practice-script-base64",
        description="""The script to run on Gaia Security Gateways during the Compliance scans in Base64. Available only for user-defined best practices.""",
    )
    regulations: list[dict] = Field(
        alias="regulations",
        description="""The applicable regulations of the Gaia Best Practice. Appear only when the value of the 'details-level' parameter is set to 'full'.""",
    )
    relevant_objects: list[dict] = Field(
        alias="relevant-objects",
        description="""The applicable objects of the Gaia Best Practice. Appear only when the value of the 'details-level' parameter is set to 'full'.""",
    )
    status: str = Field(
        alias="status", description="""The current status of the Best Practice."""
    )
    user_defined: bool = Field(
        alias="user-defined",
        description="""Determines if the Gaia Best Practice is a user-defined best practice.""",
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
