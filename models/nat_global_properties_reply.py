from pydantic import BaseModel, Field


class NatGlobalPropertiesReply(BaseModel):
    allow_bi_directional_nat: bool = Field(
        alias="allow-bi-directional-nat",
        description="""Applies to automatic NAT rules in the NAT Rule Base, and allows two automatic NAT rules to match a connection. Without Bidirectional NAT, only one automatic NAT rule can match a connection.""",
    )
    auto_arp_conf: bool = Field(
        alias="auto-arp-conf",
        description="""Ensures that ARP requests for a translated (NATed) machine, network or address range are answered by the Check Point Security Gateway.""",
    )
    merge_manual_proxy_arp_conf: bool = Field(
        alias="merge-manual-proxy-arp-conf",
        description="""Merges the automatic and manual ARP configurations. Manual proxy ARP configuration is required for manual Static NAT rules.<br>Available only if auto-arp-conf is true.""",
    )
    auto_translate_dest_on_client_side: bool = Field(
        alias="auto-translate-dest-on-client-side",
        description="""Applies to packets originating at the client, with the server as its destination. Static NAT for the server is performed on the client side.""",
    )
    manually_translate_dest_on_client_side: bool = Field(
        alias="manually-translate-dest-on-client-side",
        description="""Applies to packets originating at the client, with the server as its destination. Static NAT for the server is performed on the client side.""",
    )
    enable_ip_pool_nat: bool = Field(
        alias="enable-ip-pool-nat",
        description="""Applies to packets originating at the client, with the server as its destination. Static NAT for the server is performed on the client side.""",
    )
    addr_alloc_and_release_track: str = Field(
        alias="addr-alloc-and-release-track",
        description="""Specifies whether to log each allocation and release of an IP address from the IP Pool.<br>Available only if enable-ip-pool-nat is true.""",
    )
    addr_exhaustion_track: str = Field(
        alias="addr-exhaustion-track",
        description="""Specifies the action to take if the IP Pool is exhausted.<br>Available only if enable-ip-pool-nat is true.""",
    )
