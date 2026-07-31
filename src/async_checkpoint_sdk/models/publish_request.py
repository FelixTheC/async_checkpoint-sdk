from .pydantic import BaseModel, Field


class PublishRequest(BaseModel):
    uid: str = Field(
        alias="uid",
        description="""Session unique identifier. Specify it to publish a different session than the one you currently use.""",
    )
