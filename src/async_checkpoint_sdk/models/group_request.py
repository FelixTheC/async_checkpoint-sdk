from pydantic import BaseModel, Field


class GroupRequest(BaseModel):
    by: list[str] = Field(alias="by", description="""The fields to group by.""")
    group_limit: int = Field(
        alias="group-limit", description="""Limit the number of groups to be retrieved."""
    )
