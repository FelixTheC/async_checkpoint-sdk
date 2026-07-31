from indicator_observable_request import IndicatorObservableRequest
from indicator_override_request import IndicatorOverrideRequest
from pydantic import BaseModel, Field


class IndicatorRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    observables: IndicatorObservableRequest | list[dict] = Field(
        alias="observables", description="""The indicator's observables."""
    )
    action: str = Field(alias="action", description="""The indicator's action.""")
    profile_overrides: IndicatorOverrideRequest | list[dict] = Field(
        alias="profile-overrides",
        description="""Profiles in which to override the indicator's default action.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
