from pydantic import BaseModel, Field


class ApiQueryOrderRequest(BaseModel):
    asc: str = Field(
        alias="ASC",
        description="""Sorts results by the given field in ascending order.""",
    )
