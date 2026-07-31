from pydantic import BaseModel, Field


class SortRequest(BaseModel):
    order: str = Field(alias="order", description="""The order of the sort.""")
