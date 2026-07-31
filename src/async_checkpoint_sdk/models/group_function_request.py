from pydantic import BaseModel, Field


class GroupFunctionRequest(BaseModel):
    fields: list[str] = Field(alias="fields", description="""Actual fields returned.""")
    function: str = Field(
        alias="function",
        description="""The function used to gather the values from the records of the group.""",
    )
