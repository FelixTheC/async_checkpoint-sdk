from pydantic import BaseModel, Field


class VptSetPhysInterfaceRequest(BaseModel):
    name: str = Field(alias="name", description="""Name of the interface.""")
    vlan_trunk: bool = Field(
        alias="vlan-trunk", description="""True if this interface is a VLAN trunk."""
    )
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or Cluster object."""
    )
