from pydantic import BaseModel, Field


class CloneAccessLayerRequest(BaseModel):
    name: str = Field(alias="name", description="""The name of the layer to be cloned.""")
    new_name: str = Field(alias="new-name", description="""The name of the cloned layer.""")
