from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class KeyWordsDataTypeRequestEdit(BaseModel):
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    description: str = Field(
        alias="description",
        description="""For built-in data types, the description explains the purpose of this type of data representation.
For custom-made data types, you can use this field to provide more details.""",
    )
    keywords: add | remove | str | list[str] = Field(
        alias="keywords", description="""Specify keywords or phrases to search for."""
    )
    data_match_threshold: str = Field(
        alias="data-match-threshold",
        description="""If set to all-keywords - the data will be matched to the rule only if all the words in the list appear in the data contents.
When set to min-keywords any number of the words may appear according to configuration.""",
    )
    min_number_of_keywords: int = Field(
        alias="min-number-of-keywords",
        description="""Define how many of the words in the list must appear in the contents of the data to match the rule.""",
    )
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
