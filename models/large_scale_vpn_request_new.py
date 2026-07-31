from object import Object
from pydantic import BaseModel, Field
from vpn_domain_request import VpnDomainRequest


class LargeScaleVpnRequestNew(BaseModel):
    allowed_ip_addresses: str | list[str] = Field(
        alias="allowed-ip-addresses",
        description="""Collection of network objects identified by name or UID that represent IP addresses allowed in profile's VPN domain.""",
    )
    restrict_allowed_addresses: bool = Field(
        alias="restrict-allowed-addresses",
        description="""Indicate whether the IP addresses allowed in the VPN Domain will be restricted or not, according to allowed-ip-addresses field.""",
    )
    vpn_domain: VpnDomainRequest = Field(
        alias="vpn-domain", description="""peers' VPN Domain properties."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: Object = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
