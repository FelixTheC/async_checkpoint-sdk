from pydantic import BaseModel, Field


class LoginTokenRequest(BaseModel):
    domain: str = Field(alias="domain", description="""N/A""")
