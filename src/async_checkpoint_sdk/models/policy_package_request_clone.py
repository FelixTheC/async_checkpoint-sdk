from pydantic import BaseModel, Field


class PolicyPackageRequestClone(BaseModel):
    name: str = Field(alias="name", description="""The name of the policy package to be cloned.""")
    new_name: str = Field(
        alias="new-name", description="""The name of the cloned policy package."""
    )
