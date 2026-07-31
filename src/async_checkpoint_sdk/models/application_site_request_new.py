from .pydantic import BaseModel, Field


class ApplicationSiteRequestNew(BaseModel):
    additional_categories: str | list[str] = Field(
        alias="additional-categories",
        description="""Used to configure or edit the additional categories of a custom application / site used in the Application and URL Filtering or Threat Prevention.""",
    )
    description: str = Field(
        alias="description", description="""A description for the application."""
    )
    urls_defined_as_regular_expression: bool = Field(
        alias="urls-defined-as-regular-expression",
        description="""States whether the URL is defined as a Regular Expression or not.""",
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
    groups: str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
