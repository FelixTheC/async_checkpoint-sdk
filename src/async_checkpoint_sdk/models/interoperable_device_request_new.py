from .interoperable_interface_request import InteroperableInterfaceRequest
from .pydantic import BaseModel, Field
from .vpn_settings_request import VpnSettingsRequest


class InteroperableDeviceRequestNew(BaseModel):
    autonomous_system_number: str = Field(
        alias="autonomous-system-number",
        description="""The Autonomous System Number (ASN) for this Interoperable Device object.""",
    )
    interfaces: InteroperableInterfaceRequest | list[dict] = Field(
        alias="interfaces", description="""Network interfaces."""
    )
    vpn_settings: VpnSettingsRequest = Field(
        alias="vpn-settings",
        description="""VPN domain properties for the Interoperable Device.""",
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
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    groups: str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
