from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class ApplicationSiteRequestEdit(BaseModel):
    additional_categories: add | remove | str | list[str] = Field(
        alias="additional-categories",
        description="""Used to configure or edit the additional categories of a custom application / site used in the Application and URL Filtering or Threat Prevention.""",
    )
    description: str = Field(
        alias="description", description="""A description for the application."""
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    primary_category: str = Field(
        alias="primary-category",
        description="""Each application is assigned to one primary category based on its most defining aspect.""",
    )
    url_list: add | remove | str | list[str] = Field(
        alias="url-list",
        description="""URLs that determine this particular application.""",
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
    groups: add | remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
