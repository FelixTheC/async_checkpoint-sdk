from .pydantic import BaseModel, Field


class NetworkObjectPackagesAndDetails(BaseModel):
    name: str = Field(alias="name", description="""The target object name.""")
    uid: str = Field(alias="uid", description="""The target object unique identifier.""")
