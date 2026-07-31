from .advanced_action_settings_reply import AdvancedActionSettingsReply
from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .custom_summary_fields_reply import CustomSummaryFieldsReply
from .expiration_date_reply import ExpirationDateReply
from .hits_reply import HitsReply
from .ip_ranges import IpRanges
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .object import Object
from .port_ranges import PortRanges
from .pydantic import BaseModel, Field
from .user_check_reply import UserCheckReply


class AccessRuleReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    action: ApiObjectStandardIdentifier = Field(
        alias="action",
        description="""Accept, Drop, Ask, Inform, Reject, User Auth, Client Auth, Apply Layer. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    action_settings: AdvancedActionSettingsReply = Field(
        alias="action-settings", description="""Action settings."""
    )
    content: list[dict] = Field(
        alias="content",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    content_direction: str = Field(
        alias="content-direction",
        description="""On which direction the file types processing is applied.""",
    )
    content_negate: bool = Field(
        alias="content-negate", description="""True if negate is set for data."""
    )
    custom_fields: CustomSummaryFieldsReply = Field(
        alias="custom-fields", description="""Custom fields."""
    )
    destination: list[dict] = Field(
        alias="destination",
        description="""Collection of Network objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    destination_negate: bool = Field(
        alias="destination-negate",
        description="""True if negate is set for destination.""",
    )
    destination_ranges: IpRanges = Field(
        alias="destination-ranges",
        description="""Displays the destination as ranges of IP addresses, in case show-as-ranges is set to true.<br />In this case, 'destination' and 'destination-negate' parameters are omitted.""",
    )
    enabled: bool = Field(alias="enabled", description="""Enable/Disable the rule.""")
    expiration_settings: ExpirationDateReply = Field(
        alias="expiration-settings",
        description="""Displays the expiration date settings.""",
    )
    hits: HitsReply = Field(alias="hits", description="""Hits count object.""")
    inline_layer: ApiObjectStandardIdentifier = Field(
        alias="inline-layer",
        description="""Inline Layer identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    install_on: list[dict] = Field(
        alias="install-on",
        description="""Which gateway, identified by the name or UID, to install the policy. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    layer: str = Field(alias="layer", description="""N/A""")
    service: list[dict] = Field(
        alias="service",
        description="""Collection of Network objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    service_negate: bool = Field(
        alias="service-negate", description="""True if negate is set for service."""
    )
    service_ranges: PortRanges = Field(
        alias="service-ranges",
        description="""Displays the services and applications as ranges of port numbers, in case show-as-ranges is set to true.<br />In this case, 'service' and 'service-negate' parameters are omitted.""",
    )
    service_resource: ApiObjectStandardIdentifier = Field(
        alias="service-resource", description="""Resource of the service."""
    )
    source: list[dict] = Field(
        alias="source",
        description="""Collection of Network objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    source_negate: bool = Field(
        alias="source-negate", description="""True if negate is set for source."""
    )
    source_ranges: IpRanges = Field(
        alias="source-ranges",
        description="""Displays the source as ranges of IP addresses, in case show-as-ranges is set to true.<br />In this case, 'source' and 'source-negate' parameters are omitted.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    time: list[dict] = Field(
        alias="time",
        description="""List of time objects. For example: Weekend, Off-Work, Every-Day. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    track: Object = Field(alias="track", description="""Track Settings.""")
    user_check: UserCheckReply = Field(alias="user-check", description="""UserCheck settings.""")
    vpn: list[dict] = Field(
        alias="vpn",
        description="""VPN settings. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
