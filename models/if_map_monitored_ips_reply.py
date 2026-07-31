from pydantic import BaseModel, Field


class IfMapMonitoredIpsReply(BaseModel):
    first_ip: str = Field(
        alias="first-ip",
        description="""First IPv4 address in the range to be monitored.""",
    )
    last_ip: str = Field(
        alias="last-ip",
        description="""Last IPv4 address in the range to be monitored.""",
    )
