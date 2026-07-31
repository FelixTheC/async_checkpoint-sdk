from .probing_settings_request_new import ProbingSettingsRequestNew
from .pydantic import BaseModel, Field


class LinkSelectionRequestNew(BaseModel):
    ip_selection: str = Field(alias="ip-selection", description="""N/A""")
    ip_address: str = Field(
        alias="ip-address",
        description="""IP Address. Must be set when ip-selection was selected to be use-selected-address-from-topology or use-statically-nated-ip.""",
    )
    dns_resolving_hostname: str = Field(
        alias="dns-resolving-hostname",
        description="""DNS Resolving Hostname. Must be set when ip-selection was selected to be dns-resolving-from-hostname.""",
    )
    probing_settings: ProbingSettingsRequestNew = Field(
        alias="probing-settings",
        description="""Probing settings configuration. Only available when ip-selection is 'use-probing-with-high-availability' or 'use-probing-with-load-sharing'.""",
    )
    route_selection_method: str = Field(
        alias="route-selection-method",
        description="""Outgoing route selection method when initiating a tunnel: 'os-routing-table' (uses routing table with lowest metric) or 'route-based-probing' (checks link activity before selecting best active route).""",
    )
    responding_traffic: str = Field(
        alias="responding-traffic",
        description="""Method for handling responding traffic. Only applicable when using OS routing table.""",
    )
    source_ip_selection: str = Field(
        alias="source-ip-selection",
        description="""Source IP selection configuration for outgoing VPN traffic.""",
    )
    selected_ip: str = Field(
        alias="selected-ip",
        description="""Selected IP address. Required when source-ip-selection mode is 'specific-ip'.""",
    )
    outgoing_link_tracking: str = Field(
        alias="outgoing-link-tracking",
        description="""Outgoing link tracking - logs resolving decisions and link changes for VPN peers. Creates log entries when links become unavailable and new links are chosen.""",
    )
