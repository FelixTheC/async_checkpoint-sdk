from pydantic import BaseModel, Field


class VsxDowngradeRequest(BaseModel):
    target_version: str = Field(alias="target-version", description="""The target version.""")
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or VSX Cluster object."""
    )
