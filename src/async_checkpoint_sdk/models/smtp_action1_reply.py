from pydantic import BaseModel, Field
from smtp_rewrite_custom_header_reply import SmtpRewriteCustomHeaderReply
from smtp_rewrite_header_reply import SmtpRewriteHeaderReply


class SmtpAction1Reply(BaseModel):
    sender: SmtpRewriteHeaderReply = Field(alias="sender", description="""Rewrite Sender header.""")
    recipient: SmtpRewriteHeaderReply = Field(
        alias="recipient", description="""Rewrite Recipient header."""
    )
    custom_field: SmtpRewriteCustomHeaderReply = Field(
        alias="custom-field", description="""The name of the header."""
    )
