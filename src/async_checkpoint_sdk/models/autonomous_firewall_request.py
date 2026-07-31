from pydantic import BaseModel, Field


class AutonomousFirewallRequest(BaseModel):
    domain: str = Field(alias="domain", description="""N/A""")
    session_id: str = Field(alias="session-id", description="""N/A""")
