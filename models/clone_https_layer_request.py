from pydantic import BaseModel, Field


class CloneHttpsLayerRequest(BaseModel):
    new_name: str = Field(
        alias="new-name", description="""The name of the cloned layer."""
    )
