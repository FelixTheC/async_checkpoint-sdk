from add import Add
from keywords_and_phrases_request_for_edit import KeywordsAndPhrasesRequestForEdit
from pydantic import BaseModel, Field
from remove import Remove


class WeightedWordsRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    description: str = Field(
        alias="description",
        description="""For built-in data types, the description explains the purpose of this type of data representation.
For custom-made data types, you can use this field to provide more details.""",
    )
    weighted_keywords: Add | Remove | KeywordsAndPhrasesRequestForEdit | list[dict] = Field(
        alias="weighted-keywords", description="""List of keywords or phrases."""
    )
    sum_of_weights_threshold: int = Field(
        alias="sum-of-weights-threshold",
        description="""Define the number of appearances, by weight, of all the keywords that, beyond this threshold,
 the data containing this list of words or phrases will be recognized as data to be protected.""",
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
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
