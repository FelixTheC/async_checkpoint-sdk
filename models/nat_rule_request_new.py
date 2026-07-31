from pydantic import BaseModel, Field


class NatRuleRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Rule name.""")
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    install_on: str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    method: str = Field(alias="method", description="""Nat method.""")
    original_destination: str = Field(
        alias="original-destination", description="""Original destination."""
    )
    original_service: str = Field(
        alias="original-service", description="""Original service."""
    )
    original_source: str = Field(
        alias="original-source", description="""Original source."""
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    translated_destination: str = Field(
        alias="translated-destination", description="""Translated  destination."""
    )
    translated_service: str = Field(
        alias="translated-service", description="""Translated  service."""
    )
    translated_source: str = Field(
        alias="translated-source", description="""Translated  source."""
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
