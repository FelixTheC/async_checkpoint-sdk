from pydantic import BaseModel, Field


class ServiceGroupRequestShow(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    show_as_ranges: bool = Field(
        alias="show-as-ranges",
        description="""When true, the service group's matched content is displayed as ranges of port numbers rather than service objects.<br />Objects that are not represented using port numbers are presented as objects.<br />The 'members' parameter is omitted from the response and instead the 'ranges' parameter is displayed.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
