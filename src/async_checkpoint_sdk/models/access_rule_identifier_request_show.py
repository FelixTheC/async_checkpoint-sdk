from .hits_settings_request import HitsSettingsRequest
from .pydantic import BaseModel, Field


class AccessRuleIdentifierRequestShow(BaseModel):
    package: str = Field(alias="package", description="""Policy package name or uid.""")
    show_as_ranges: bool = Field(
        alias="show-as-ranges",
        description="""When true, the source, destination and services & applications parameters are displayed as ranges of IP addresses and port numbers rather than network objects.<br /> Objects that are not represented using IP addresses or port numbers are presented as objects.<br /> In addition, the response of each rule does not contain the parameters: source, source-negate, destination, destination-negate, service and service-negate, but instead it contains the parameters: source-ranges, destination-ranges and service-ranges.<br /><br /> Note: Requesting to show rules as ranges is limited up to 20 rules per request, otherwise an error is returned. If you wish to request more rules, use the offset and limit parameters to limit your request.""",
    )
    show_expiration_settings: bool = Field(
        alias="show-expiration-settings",
        description="""Indicates whether to calculate and show expiration date settings field in reply.""",
    )
    show_hits: bool = Field(alias="show-hits", description="""Show hitcount data.""")
    hits_settings: HitsSettingsRequest = Field(
        alias="hits-settings",
        description="""Hitcount settings, define the range if hits to show.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
