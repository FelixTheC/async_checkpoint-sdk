from api_object_standard_identifier import ApiObjectStandardIdentifier
from optional_parameters_reply import OptionalParametersReply
from pydantic import BaseModel, Field


class OfficeModeMethodReply(BaseModel):
    radius_server: bool = Field(
        alias="radius-server",
        description="""Radius server used to authenticate the user.""",
    )
    use_allocate_method: bool = Field(
        alias="use-allocate-method", description="""Use Allocate Method."""
    )
    allocate_method: str = Field(
        alias="allocate-method",
        description="""Using either Manual (IP Pool) or Automatic (DHCP).
Must be set when use-allocate-method is true.""",
    )
    manual_network: ApiObjectStandardIdentifier = Field(
        alias="manual-network",
        description="""Manual Network. Identified by name or UID.
Must be set when allocate-method was selected to be manual.""",
    )
    dhcp_server: ApiObjectStandardIdentifier = Field(
        alias="dhcp-server",
        description="""DHCP Server. Identified by name or UID.
Must be set when allocate-method was selected to be automatic.""",
    )
    virtual_ip_address: str = Field(
        alias="virtual-ip-address",
        description="""Virtual IPV4 address for DHCP server replies.
Must be set when allocate-method was selected to be automatic.""",
    )
    dhcp_mac_address: str = Field(
        alias="dhcp-mac-address",
        description="""Calculated MAC address for DHCP allocation.
Must be set when allocate-method was selected to be automatic.""",
    )
    optional_parameters: OptionalParametersReply = Field(
        alias="optional-parameters",
        description="""This configuration applies to all Office Mode methods except Automatic (using DHCP) and ipassignment.conf entries which contain this data.""",
    )
