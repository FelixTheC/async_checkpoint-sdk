from .pydantic import BaseModel, Field


class DataCenterContentRequest(BaseModel):
    limit: int = Field(alias="limit", description="""The maximal number of returned results.""")
    offset: int = Field(alias="offset", description="""Number of the results to initially skip.""")
    order: list[dict] = Field(
        alias="order",
        description="""Sorts the results by search criteria. Automatically sorts the results by Name, in the ascending order.""",
    )
    uid_in_data_center: str = Field(
        alias="uid-in-data-center",
        description="""Return result matching the unique identifier of the object on the Data Center Server.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""Standard and Full description are the same.""",
    )
