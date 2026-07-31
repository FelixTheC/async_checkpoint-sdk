from .pydantic import BaseModel, Field


class InterfaceRequestDelete(BaseModel):
    gateway_uid: str = Field(
        alias="gateway-uid",
        description="""Gateway or cluster object uid that the interface belongs to. <font color=red>Required only if</font> name was specified.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
