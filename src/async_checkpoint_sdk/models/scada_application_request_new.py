from pydantic import BaseModel, Field


class ScadaApplicationRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    category: str = Field(alias="category", description="""SCADA application category.""")
    additional_categories: str | list[str] = Field(
        alias="additional-categories",
        description="""Used to configure or edit the additional categories of a custom application / site used in the Application and URL Filtering or Threat Prevention.""",
    )
    application_signature: str = Field(alias="application-signature", description="""N/A""")
    description: str = Field(
        alias="description", description="""A description for the application."""
    )
    scada_properties: list[dict] = Field(
        alias="scada-properties", description="""SCADA application properties."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
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
