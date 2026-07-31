from pydantic import BaseModel, Field


class VptRemovePhysInterfaceRequest(BaseModel):
    name: str = Field(alias="name", description="""Name of the interface.""")
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or Cluster object."""
    )
