from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class PasscodeProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    allow_simple_passcode: bool = Field(
        alias="allow-simple-passcode",
        description="""The passcode length is 4 and only numeric values are allowed.""",
    )
    min_passcode_length: int = Field(
        alias="min-passcode-length",
        description="""Minimum passcode length - relevant if allow-simple-passcode is disabled.""",
    )
    min_passcode_complex_characters: int = Field(
        alias="min-passcode-complex-characters",
        description="""Minimum number of complex characters (if require-alphanumeric-passcode is enabled).""",
    )
    require_alphanumeric_passcode: bool = Field(
        alias="require-alphanumeric-passcode",
        description="""Require alphanumeric characters in the passcode - relevant if allow-simple-passcode is disable.""",
    )
    force_passcode_expiration: bool = Field(
        alias="force-passcode-expiration",
        description="""Enable/disable expiration date of the passcode.""",
    )
    passcode_expiration_period: int = Field(
        alias="passcode-expiration-period",
        description="""The period in days after which the passcode will expire.""",
    )
    enable_inactivity_time_lock: bool = Field(
        alias="enable-inactivity-time-lock", description="""Lock the device if app is inactive."""
    )
    max_inactivity_time_lock: int = Field(
        alias="max-inactivity-time-lock",
        description="""Time without user input before passcode must be re-entered (in minutes).""",
    )
    enable_passcode_failed_attempts: bool = Field(
        alias="enable-passcode-failed-attempts",
        description="""Exit after few failures in passcode verification.""",
    )
    max_passcode_failed_attempts: int = Field(
        alias="max-passcode-failed-attempts", description="""Number of failed attempts allowed."""
    )
    enable_passcode_history: bool = Field(
        alias="enable-passcode-history", description="""Check passcode history for reparations."""
    )
    passcode_history: int = Field(
        alias="passcode-history",
        description="""Number of passcodes that will be kept in history.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
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
