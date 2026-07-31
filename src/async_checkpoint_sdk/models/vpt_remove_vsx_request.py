from pydantic import BaseModel, Field


class VptRemoveVsxRequest(BaseModel):
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or Cluster object."""
    )
