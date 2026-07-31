from .pydantic import BaseModel, Field


class PolicyPackageRequestClone(BaseModel):
    new_name: str = Field(
        alias="new-name", description="""The name of the cloned policy package."""
    )
