from new_query_request import NewQueryRequest
from pydantic import BaseModel, Field


class ShowLogsRequest(BaseModel):
    new_query: NewQueryRequest = Field(alias="new-query", description="""Running a new query.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Ignore warnings if exist."""
    )
