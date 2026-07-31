from pydantic import BaseModel, Field


class TaskQueryRequest(BaseModel):
    initiator: str = Field(
        alias="initiator",
        description="""Initiator's name. If name isn't specified, tasks from all initiators will be shown.""",
    )
    status: str = Field(alias="status", description="""Status.""")
    from_date: str = Field(
        alias="from-date",
        description="""The date from which tracking tasks is to be performed, by the task's last update date. ISO 8601. If timezone isn't specified in the input, the Management server's timezone is used.""",
    )
    to_date: str = Field(
        alias="to-date",
        description="""The date until which tracking tasks is to be performed, by the task's last update date. ISO 8601. If timezone isn't specified in the input, the Management server's timezone is used.""",
    )
    limit: int = Field(
        alias="limit", description="""The maximal number of returned results."""
    )
    offset: int = Field(
        alias="offset", description="""Number of the results to initially skip."""
    )
    order: list[dict] = Field(
        alias="order",
        description="""Sorts results by the given field. By default the results are sorted in the descending order by the task's last update date.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
