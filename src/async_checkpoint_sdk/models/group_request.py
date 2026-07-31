from .pydantic import BaseModel, Field


class GroupRequest(BaseModel):
    group_limit: int = Field(
        alias="group-limit",
        description="""Limit the number of groups to be retrieved.""",
    )
