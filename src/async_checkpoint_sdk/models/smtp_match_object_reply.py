from .pydantic import BaseModel, Field


class SmtpMatchObjectReply(BaseModel):
    sender: str = Field(
        alias="sender",
        description="""Set the Match sender property for the SMTP resource.""",
    )
    recipient: str = Field(
        alias="recipient",
        description="""Set the Match recipient property for the SMTP resource.""",
    )
