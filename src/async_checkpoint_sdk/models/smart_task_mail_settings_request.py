from pydantic import BaseModel, Field


class SmartTaskMailSettingsRequest(BaseModel):
    recipients: str = Field(
        alias="recipients", description="""A comma separated list of recipient mail addresses."""
    )
    sender_email: str = Field(
        alias="sender-email", description="""An email address to send the mail from."""
    )
    subject: str = Field(alias="subject", description="""The email subject.""")
    body: str = Field(alias="body", description="""The email body.""")
    attachment: str = Field(
        alias="attachment", description="""What file should be attached to the mail."""
    )
    bcc_recipients: str = Field(
        alias="bcc-recipients",
        description="""A comma separated list of bcc recipient mail addresses.""",
    )
    cc_recipients: str = Field(
        alias="cc-recipients",
        description="""A comma separated list of cc recipient mail addresses.""",
    )
