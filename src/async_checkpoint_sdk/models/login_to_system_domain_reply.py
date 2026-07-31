from pydantic import BaseModel, Field


class LoginToSystemDomainReply(BaseModel):
    sid: str = Field(alias="sid", description="""Session unique identifier.""")
