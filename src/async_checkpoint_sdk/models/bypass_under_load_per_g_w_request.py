from .pydantic import BaseModel, Field


class BypassUnderLoadPerGWRequest(BaseModel):
    value: bool = Field(
        alias="value",
        description="""* true - enabled.<br>* false - disabled (default value).""",
    )
