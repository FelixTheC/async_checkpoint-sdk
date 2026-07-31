from .pydantic import BaseModel, Field


class TopRequest(BaseModel):
    count: int = Field(alias="count", description="""The number of results to retrieve.""")
