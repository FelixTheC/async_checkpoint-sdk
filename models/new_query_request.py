from group_request import GroupRequest
from pydantic import BaseModel, Field
from top_request import TopRequest


class NewQueryRequest(BaseModel):
    filter: str = Field(
        alias="filter",
        description="""The filter expression as entered in SmartConsole/SmartView.""",
    )
    time_frame: str = Field(
        alias="time-frame", description="""Specify the time frame to query logs."""
    )
    custom_start: str = Field(
        alias="custom-start",
        description="""This option is only applicable when using the custom time-frame option.""",
    )
    custom_end: str = Field(
        alias="custom-end",
        description="""This option is only applicable when using the custom time-frame option.""",
    )
    top: TopRequest = Field(alias="top", description="""Top results configuration.""")
    group: GroupRequest = Field(
        alias="group",
        description="""Specify how to group logs. Supported only in environments with SmartEvent configured.""",
    )
    sort: list[dict] = Field(
        alias="sort",
        description="""Order by fields. Applicable only for group requests.""",
    )
    returned_fields: list[str] = Field(
        alias="returned-fields",
        description="""Specifies which fields to include in the results. Not applicable when using group/top requests.""",
    )
    max_logs_per_request: int = Field(
        alias="max-logs-per-request",
        description="""Maximum number of logs to return per request.""",
    )
    show_total_record_count: bool = Field(
        alias="show-total-record-count", description="""Returns the total logs count."""
    )
    type: str = Field(alias="type", description="""Filter logs by specified type.""")
    log_servers: list[str] = Field(
        alias="log-servers", description="""Filter logs from specified log-servers."""
    )
