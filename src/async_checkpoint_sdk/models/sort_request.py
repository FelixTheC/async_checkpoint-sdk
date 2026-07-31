from pydantic import BaseModel, Field


class SortRequest(BaseModel):
    field: str = Field(alias="field", description="""The fields used to order.""")
    order: str = Field(alias="order", description="""The order of the sort.""")
