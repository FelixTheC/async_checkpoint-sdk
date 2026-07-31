from pydantic import BaseModel, Field


class SecurityGroupMembersRequest(BaseModel):
    name: str = Field(alias="name", description="""Name of the Security Group.""")
