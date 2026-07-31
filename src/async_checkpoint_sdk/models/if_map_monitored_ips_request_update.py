from .pydantic import BaseModel, Field


class IfMapMonitoredIpsRequestUpdate(BaseModel):
    new_first_ip: str = Field(
        alias="new-first-ip",
        description="""New first IPv4 address in the range to be monitored.""",
    )
    new_last_ip: str = Field(
        alias="new-last-ip",
        description="""New last IPv4 address in the range to be monitored.""",
    )
