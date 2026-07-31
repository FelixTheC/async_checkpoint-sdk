from .automatic_cancel_request import AutomaticCancelRequest
from .pydantic import BaseModel, Field
from .upgrade_messages_request import UpgradeMessagesRequest


class BackgroundUpgradeSettingsRequestEdit(BaseModel):
    messages: UpgradeMessagesRequest = Field(
        alias="messages", description="""Background upgrade messages."""
    )
    automatic_cancel_after: AutomaticCancelRequest = Field(
        alias="automatic-cancel-after",
        description="""Automatically cancel the entire background upgrade if it is not finished on time.""",
    )
