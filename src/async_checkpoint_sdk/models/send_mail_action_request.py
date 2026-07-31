from pydantic import BaseModel, Field
from smart_task_mail_settings_request import SmartTaskMailSettingsRequest


class SendMailActionRequest(BaseModel):
    mail_settings: SmartTaskMailSettingsRequest = Field(
        alias="mail-settings", description="""The required settings to send the mail by."""
    )
    smtp_server: str = Field(
        alias="smtp-server",
        description="""The UID or the name a preconfigured SMTP server object.""",
    )
