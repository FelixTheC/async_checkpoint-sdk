from pydantic import BaseModel, Field


class TopRequest(BaseModel):
    field: str = Field(
        alias="field", description="""The field on which the top command is executed."""
    )
    count: int = Field(alias="count", description="""The number of results to retrieve.""")
