from pydantic import BaseModel, Field


class TunnelDetailsReply(BaseModel):
    ip: str = Field(
        alias="ip",
        description="""IP address used for communication between the Gateway and the Management Server (used when 'auto-generate-ip=true').""",
    )
    status: str = Field(
        alias="status",
        description="""Status of communication between the Gateway and the Management Server.""",
    )
