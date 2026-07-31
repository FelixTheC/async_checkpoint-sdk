from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class UserCheckGlobalPropertiesReply(BaseModel):
    preferred_language: str = Field(
        alias="preferred-language",
        description="""The preferred language for new UserCheck message.""",
    )
    send_emails_using_mail_server: ApiObjectStandardIdentifier = Field(
        alias="send-emails-using-mail-server",
        description="""Sends email to the specified mail server.""",
    )
