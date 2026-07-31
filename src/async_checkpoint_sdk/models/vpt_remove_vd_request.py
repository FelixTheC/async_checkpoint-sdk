from pydantic import BaseModel, Field


class VptRemoveVdRequest(BaseModel):
    vd: str = Field(
        alias="vd", description="""Name of the Virtual System, Virtual Switch, or Virtual Router."""
    )
