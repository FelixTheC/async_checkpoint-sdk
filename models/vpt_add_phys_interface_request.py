from pydantic import BaseModel, Field


class VptAddPhysInterfaceRequest(BaseModel):
    vlan_trunk: bool = Field(
        alias="vlan-trunk", description="""True if this interface is a VLAN trunk."""
    )
