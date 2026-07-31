from .api_domain_identifier import ApiDomainIdentifier
from .automatic_cancel_reply import AutomaticCancelReply
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field
from .upgrade_messages_reply import UpgradeMessagesReply


class BackgroundUpgradeSettingsReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    messages: UpgradeMessagesReply = Field(
        alias="messages", description="""Background upgrade messages."""
    )
    automatic_cancel_after: AutomaticCancelReply = Field(
        alias="automatic-cancel-after",
        description="""Automatically cancel the entire background upgrade if it is not finished on time.""",
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
