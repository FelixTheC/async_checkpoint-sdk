from .pydantic import BaseModel, Field


class GroupRequestShow(BaseModel):
    show_as_ranges: bool = Field(
        alias="show-as-ranges",
        description="""When true, the group's matched content is displayed as ranges of IP addresses rather than network objects.<br />Objects that are not represented using IP addresses are presented as objects.<br />The 'members' parameter is omitted from .the response and instead the 'ranges' parameter is displayed.""",
    )
    async_response: bool = Field(
        alias="async-response",
        description="""Run command in asynchronous mode and return task UID. Use show-task command to check the progress of the task.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
