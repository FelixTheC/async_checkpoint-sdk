from add import add
from pydantic import BaseModel, Field
from remove import remove


class TrustedClientRequestEdit(BaseModel):
    domains_assignment: add | remove | str | list[str] = Field(
        alias="domains-assignment",
        description="""Domains to be added to this profile. Use domain name only. See example below: add-trusted-client (with domain).""",
    )
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.""",
    )
    ip_address_first: str = Field(
        alias="ip-address-first",
        description="""First IP address in the range. If both IPv4 and IPv6 address ranges are required, use the ipv4-address-first and the ipv6-address-first fields instead.""",
    )
    ip_address_last: str = Field(
        alias="ip-address-last",
        description="""Last IP address in the range. If both IPv4 and IPv6 address ranges are required, use the ipv4-address-first and the ipv6-address-first fields instead.""",
    )
    mask_length: int = Field(
        alias="mask-length",
        description="""IPv4 or IPv6 mask length. If both masks are required use mask-length4 and mask-length6 fields explicitly.""",
    )
    multi_domain_server_trusted_client: bool = Field(
        alias="multi-domain-server-trusted-client",
        description="""Let this trusted client connect to all Multi-Domain Servers in the deployment.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    subnet_mask: str = Field(alias="subnet-mask", description="""N/A""")
    subnet_mask4: str = Field(alias="subnet-mask4", description="""N/A""")
    type: str = Field(alias="type", description="""Trusted client type.""")
    wild_card: str = Field(
        alias="wild-card", description="""IP wild card (e.g. 192.0.2.*)."""
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
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
