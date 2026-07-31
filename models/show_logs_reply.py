from object import Object
from pydantic import BaseModel, Field


class ShowLogsReply(BaseModel):
    incidents: Object = Field(
        alias="incidents",
        description="""Incident object when error or warning occur.""",
    )
    logs: Object = Field(alias="logs", description="""Logs result.""")
    logs_count: int = Field(
        alias="logs-count", description="""Number of logs in the result."""
    )
    query_id: str = Field(
        alias="query-id",
        description="""Get the next page of last run query with specified limit.""",
    )
    reach_group_limit: bool = Field(
        alias="reach-group-limit",
        description="""Indicates if the response include all possible answers.""",
    )
    response_group_limit: int = Field(
        alias="response-group-limit", description="""Shows the chosen group limit."""
    )
    statistics: Object = Field(
        alias="statistics", description="""Grouping statistics."""
    )
    tops: Object = Field(alias="tops", description="""Tops result.""")
    tops_count: int = Field(
        alias="tops-count", description="""Total logs in top response."""
    )
