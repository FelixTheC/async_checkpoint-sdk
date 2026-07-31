from api_object_standard_identifier import ApiObjectStandardIdentifier
from office_mode_method_reply import OfficeModeMethodReply
from pydantic import BaseModel, Field


class OfficeModeReply(BaseModel):
    mode: str = Field(
        alias="mode",
        description="""Office Mode Permissions.
When selected to be off, all the other definitions are irrelevant.""",
    )
    group: ApiObjectStandardIdentifier = Field(
        alias="group",
        description="""Group. Identified by name or UID.
Must be set when office-mode-permissions was selected to be group.""",
    )
    allocate_ip_address_from: OfficeModeMethodReply = Field(
        alias="allocate-ip-address-from",
        description="""Allocate IP address Method.
Allocate IP address by sequentially trying the given methods until success.""",
    )
    support_multiple_interfaces: bool = Field(
        alias="support-multiple-interfaces",
        description="""Support connectivity enhancement for gateways with multiple external interfaces.""",
    )
    perform_anti_spoofing: bool = Field(
        alias="perform-anti-spoofing",
        description="""Perform Anti-Spoofing on Office Mode addresses.""",
    )
    anti_spoofing_additional_addresses: ApiObjectStandardIdentifier = Field(
        alias="anti-spoofing-additional-addresses",
        description="""Additional IP Addresses for Anti-Spoofing.
Identified by name or UID.
Must be set when perform-anti-spoofings is true.""",
    )
