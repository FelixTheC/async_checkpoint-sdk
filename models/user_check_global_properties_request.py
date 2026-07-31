from pydantic import BaseModel, Field


class UserCheckGlobalPropertiesRequest(BaseModel):
    preferred_language: str = Field(
        alias="preferred-language",
        description="""The preferred language for new UserCheck message.""",
    )
    send_emails_using_mail_server: str = Field(
        alias="send-emails-using-mail-server",
        description="""Name or UID of mail server to send emails to.""",
    )
