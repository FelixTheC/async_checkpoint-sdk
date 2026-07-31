from advanced_action_settings_request import AdvancedActionSettingsRequest
from custom_summary_fields_request import CustomSummaryFieldsRequest
from object import Object
from pydantic import BaseModel, Field
from track_settings_for_request import TrackSettingsForRequest
from user_check_request import UserCheckRequest
from vpn_request import VpnRequest


class AccessRuleRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Rule name.""")
    action: str = Field(
        alias="action",
        description="""Accept, Drop, Ask, Inform, Reject, User Auth, Client Auth, Apply Layer.""",
    )
    action_settings: AdvancedActionSettingsRequest = Field(
        alias="action-settings", description="""Action settings."""
    )
    content: Object = Field(
        alias="content",
        description="""List of processed file types that this rule applies on.""",
    )
    content_direction: str = Field(
        alias="content-direction",
        description="""On which direction the file types processing is applied.""",
    )
    content_negate: bool = Field(
        alias="content-negate", description="""True if negate is set for data."""
    )
    custom_fields: CustomSummaryFieldsRequest = Field(
        alias="custom-fields", description="""Custom fields."""
    )
    destination: str | list[str] = Field(
        alias="destination",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate",
        description="""True if negate is set for destination.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    inline_layer: str = Field(
        alias="inline-layer",
        description="""Inline Layer identified by the name or UID. Relevant only if Action was set to Apply Layer.""",
    )
    install_on: str | list[str] = Field(
        alias="install-on",
        description="""Which Gateways identified by the name or UID to install the policy on.""",
    )
    service: str | list[str] = Field(
        alias="service",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""True if negate is set for service."""
    )
    service_resource: str = Field(
        alias="service-resource",
        description="""Resource of the service identified by the name or UID. When a service-resource exists, the service parameter should contains exactly one service element.""",
    )
    source: str | list[str] = Field(
        alias="source",
        description="""Collection of Network objects identified by the name or UID.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""True if negate is set for source."""
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    time: str | list[str] = Field(
        alias="time",
        description="""List of time objects. For example: Weekend, Off-Work, Every-Day.""",
    )
    track: TrackSettingsForRequest = Field(
        alias="track", description="""Track Settings."""
    )
    user_check: UserCheckRequest = Field(
        alias="user-check", description="""UserCheck settings."""
    )
    vpn: str | VpnRequest | list[dict] = Field(
        alias="vpn", description="""Communities or Directional."""
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
