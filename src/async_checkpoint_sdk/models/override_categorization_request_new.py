from pydantic import BaseModel, Field


class OverrideCategorizationRequestNew(BaseModel):
    url: str = Field(
        alias="url",
        description="""The URL for which we want to update the category and risk definitions, the URL and the object name are the same for Override Categorization.""",
    )
    url_defined_as_regular_expression: bool = Field(
        alias="url-defined-as-regular-expression",
        description="""States whether the URL is defined as a Regular Expression or not.""",
    )
    new_primary_category: str = Field(
        alias="new-primary-category",
        description="""Uid or name of the primary category based on its most defining aspect.""",
    )
    risk: str = Field(alias="risk", description="""States the override categorization risk.""")
    additional_categories: str | list[str] = Field(
        alias="additional-categories",
        description="""Uid or name of the categories to override in the Application and URL Filtering or Threat Prevention.""",
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
