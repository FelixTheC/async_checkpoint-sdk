from .pydantic import BaseModel, Field


class SmartTaskMailSettingsRequest(BaseModel):
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
