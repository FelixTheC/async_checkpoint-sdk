from pydantic import BaseModel, Field


class FileDataTypeRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    description: str = Field(
        alias="description",
        description="""For built-in data types, the description explains the purpose of this type of data representation.
For custom-made data types, you can use this field to provide more details.""",
    )
    match_by_file_type: bool = Field(
        alias="match-by-file-type", description="""Determine whether to consider file type."""
    )
    file_groups_list: str | list[str] = Field(
        alias="file-groups-list",
        description="""The file must be one of the types specified in the list.
Identified by name or UID.""",
    )
    match_by_file_name: bool = Field(
        alias="match-by-file-name", description="""Determine whether to consider file name."""
    )
    file_name_contains: str = Field(
        alias="file-name-contains", description="""File name should contain the expression."""
    )
    match_by_file_size: bool = Field(
        alias="match-by-file-size", description="""Determine whether to consider file size."""
    )
    file_size: int = Field(alias="file-size", description="""Min File size in KB.""")
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
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
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
