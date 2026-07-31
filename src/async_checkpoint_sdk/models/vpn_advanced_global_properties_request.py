from pydantic import BaseModel, Field


class VpnAdvancedGlobalPropertiesRequest(BaseModel):
    allow_clear_traffic_to_encryption_domain_when_disconnected: bool = Field(
        alias="allow-clear-traffic-to-encryption-domain-when-disconnected",
        description="""SecuRemote/SecureClient behavior while disconnected - How traffic to the VPN domain is handled when the Remote Access VPN client is not connected to the site. Traffic can either be dropped or sent in clear without encryption.""",
    )
    enable_load_distribution_for_mep_conf: bool = Field(
        alias="enable-load-distribution-for-mep-conf",
        description="""Load distribution for Multiple Entry Points configurations - Remote access clients will randomly select a gateway from the list of entry points. Make sure to define the same VPN domain for all the Security Gateways you want to be entry points.""",
    )
    use_first_allocated_om_ip_addr_for_all_conn_to_the_gws_of_the_site: bool = Field(
        alias="use-first-allocated-om-ip-addr-for-all-conn-to-the-gws-of-the-site",
        description="""Use first allocated Office Mode IP Address for all connections to the Gateways of the site.After a remote user connects and receives an Office Mode IP address from a gateway, every connection to that gateways encryption domain will go out with the Office Mode IP as the internal source IP. The Office Mode IP is what hosts in the encryption domain will recognize as the remote user's IP address. The Office Mode IP address assigned by a specific gateway can be used in its own encryption domain and in neighboring encryption domains as well. The neighboring encryption domains should reside behind gateways that are members of the same VPN community as the assigning gateway. Since the remote hosts connections are dependant on the Office Mode IP address it received, should the gateway that issued the IP become unavailable, all the connections to the site will terminate.""",
    )
