from pydantic import BaseModel, Field


class SecurityGroupPartitionInfoReply(BaseModel):
    msg: str = Field(
        alias="msg", description="""Used disk space of whole size of this partition."""
    )
    path: str = Field(alias="path", description="""Path of this partition.""")
    status: str = Field(
        alias="status",
        description="""Status of this path partition of current member.""",
    )
    usage: int = Field(
        alias="usage", description="""Usage in percentage of this partition."""
    )
