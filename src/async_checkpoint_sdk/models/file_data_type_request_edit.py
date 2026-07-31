from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class FileDataTypeRequestEdit(BaseModel):
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    description: str = Field(
        alias="description",
        description="""For built-in data types, the description explains the purpose of this type of data representation.
For custom-made data types, you can use this field to provide more details.""",
    )
    match_by_file_type: bool = Field(
        alias="match-by-file-type",
        description="""Determine whether to consider file type.""",
    )
    file_groups_list: add | remove | str | list[str] = Field(
        alias="file-groups-list",
        description="""The file must be one of the types specified in the list.
Identified by name or UID.""",
    )
    match_by_file_name: bool = Field(
        alias="match-by-file-name",
        description="""Determine whether to consider file name.""",
    )
    file_name_contains: str = Field(
        alias="file-name-contains",
        description="""File name should contain the expression.""",
    )
    match_by_file_size: bool = Field(
        alias="match-by-file-size",
        description="""Determine whether to consider file size.""",
    )
    file_size: int = Field(alias="file-size", description="""Min File size in KB.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
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
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
