from .pydantic import BaseModel, Field


class IfMapServerAuthenticationRequest(BaseModel):
    authentication_method: str = Field(
        alias="authentication-method",
        description="""Authentication method for the IF-MAP server.""",
    )
    username: str = Field(
        alias="username",
        description="""Username for the IF-MAP server authentication. <font color=red>Required only when</font> 'authentication-method' is set to 'basic'.""",
    )
    password: str = Field(
        alias="password",
        description="""Username for the IF-MAP server authentication. <font color=red>Required only when</font> 'authentication-method' is set to 'basic'.""",
    )
