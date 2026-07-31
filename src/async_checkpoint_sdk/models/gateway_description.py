from .pydantic import BaseModel, Field


class GatewayDescription(BaseModel):
    name: str = Field(alias="name", description="""Gateway or cluster name.""")
    type: str = Field(alias="type", description="""Gateway or cluster type.""")
    uid: str = Field(alias="uid", description="""Gateway or cluster object uid.""")
