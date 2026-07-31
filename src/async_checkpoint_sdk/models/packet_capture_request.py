from pydantic import BaseModel, Field


class PacketCaptureRequest(BaseModel):
    attachment_id: str = Field(
        alias="attachment-id", description="""Attachment identifier from a log record."""
    )
