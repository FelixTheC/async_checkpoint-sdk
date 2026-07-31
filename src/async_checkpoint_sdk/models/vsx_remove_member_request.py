from pydantic import BaseModel, Field


class VsxRemoveMemberRequest(BaseModel):
    member_uid: str = Field(
        alias="member-uid", description="""UID of the VSX Cluster member object."""
    )
