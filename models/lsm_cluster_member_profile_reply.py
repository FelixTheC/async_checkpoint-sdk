from pydantic import BaseModel, Field


class LsmClusterMemberProfileReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    ip_address: str = Field(alias="ip-address", description="""N/A""")
    comments: str = Field(alias="comments", description="""Comments string.""")
