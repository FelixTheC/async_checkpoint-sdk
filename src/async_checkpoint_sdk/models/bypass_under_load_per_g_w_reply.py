from pydantic import BaseModel, Field


class BypassUnderLoadPerGWReply(BaseModel):
    value: bool = Field(alias="value", description="""* true - enabled.<br>* false - disabled.""")
