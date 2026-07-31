from pydantic import BaseModel, Field


class GetPlatformRequest(BaseModel):
    uid: str = Field(
        alias="uid", description="""Gateway, cluster or Check Point host unique identifier."""
    )
