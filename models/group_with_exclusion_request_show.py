from pydantic import BaseModel, Field


class GroupWithExclusionRequestShow(BaseModel):
    show_as_ranges: bool = Field(
        alias="show-as-ranges",
        description="""When true, the group with exclusion's matched content is displayed as ranges of IP addresses rather than network objects.<br />Objects that are not represented using IP addresses are presented as objects.<br />The 'include' and 'except' parameters are omitted from the response and instead the 'ranges' parameter is displayed.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
