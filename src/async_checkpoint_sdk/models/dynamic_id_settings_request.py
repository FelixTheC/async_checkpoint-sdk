from pydantic import BaseModel, Field


class DynamicIdSettingsRequest(BaseModel):
    send_sms: bool = Field(alias="send-sms", description="""Whether to send SMS for Dynamic ID.""")
    send_email: bool = Field(
        alias="send-email", description="""Whether to send email for Dynamic ID."""
    )
