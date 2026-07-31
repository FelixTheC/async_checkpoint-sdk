from pydantic import BaseModel, Field
from smtp_rewrite_custom_header_request import SmtpRewriteCustomHeaderRequest
from smtp_rewrite_header_request import SmtpRewriteHeaderRequest


class SmtpAction1Request(BaseModel):
    sender: SmtpRewriteHeaderRequest = Field(
        alias="sender", description="""Rewrite Sender header."""
    )
    recipient: SmtpRewriteHeaderRequest = Field(
        alias="recipient", description="""Rewrite Recipient header."""
    )
    custom_field: SmtpRewriteCustomHeaderRequest = Field(
        alias="custom-field", description="""The name of the header."""
    )
