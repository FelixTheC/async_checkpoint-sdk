from pydantic import BaseModel, Field


class VptAttachBridgeRequest(BaseModel):
    ifs1: str = Field(alias="ifs1", description="""Name of the first interface for the bridge.""")
    ifs2: str = Field(alias="ifs2", description="""Name of the second interface for the bridge.""")
    vd: str = Field(
        alias="vd", description="""Name of the Virtual System, Virtual Switch, or Virtual Router."""
    )
