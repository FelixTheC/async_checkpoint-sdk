from pydantic import BaseModel, Field


class LoginTokenReply(BaseModel):
    login_token: str = Field(alias="login-token", description="""N/A""")
