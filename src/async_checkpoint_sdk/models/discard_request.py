from .pydantic import BaseModel, Field


class DiscardRequest(BaseModel):
    uid: str = Field(
        alias="uid",
        description="""Session unique identifier. Specify it to discard a different session than the one you currently use.""",
    )
