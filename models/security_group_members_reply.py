from pydantic import BaseModel, Field


class SecurityGroupMembersReply(BaseModel):
    members_list: list[dict] = Field(
        alias="members-list",
        description="""List of Security Group Members and their details.""",
    )
