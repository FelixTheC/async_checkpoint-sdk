from pydantic import BaseModel, Field


class VptRemoveVdInterfaceRequest(BaseModel):
    leads_to: str = Field(
        alias="leads-to", description="""Virtual Switch or Virtual Router for this interface."""
    )
    vd: str = Field(
        alias="vd", description="""Name of the Virtual System, Virtual Switch, or Virtual Router."""
    )
