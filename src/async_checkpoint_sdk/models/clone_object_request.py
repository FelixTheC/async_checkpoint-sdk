from pydantic import BaseModel, Field


class CloneObjectRequest(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    type: str = Field(
        alias="type",
        description="""Type of the cloned object.<br><font color=red>Required only when</font> identifying object by name.""",
    )
    new_name: str = Field(alias="new-name", description="""Name of the created object.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
