from .pydantic import BaseModel, Field
from .security_server_global_properties_request import (
    SecurityServerGlobalPropertiesRequest,
)


class FirewallGlobalPropertiesRequest(BaseModel):
    accept_control_connections: bool = Field(
        alias="accept-control-connections",
        description="""Used for:<br>&nbsp;&nbsp;&nbsp;&nbsp; <ul><li> Installing the security policy from .the Security Management server to the gateways.</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Sending logs from .the gateways to the Security Management server.</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Communication between SmartConsole clients and the Security Management Server</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Communication between Firewall daemons on different machines (Security Management Server, Security Gateway).</li><br>&nbsp;&nbsp;&nbsp;&nbsp; <li> Connecting to OPSEC applications such as RADIUS and TACACS authentication servers.</li></ul>If you disable Accept Control Connections and you want Check Point components to communicate with each other and with OPSEC components, you must explicitly allow these connections in the Rule Base.""",
    )
    accept_ips1_management_connections: bool = Field(
        alias="accept-ips1-management-connections",
        description="""Accepts IPS-1 connections.<br>Available only if accept-control-connections is true.""",
    )
    accept_remote_access_control_connections: bool = Field(
        alias="accept-remote-access-control-connections",
        description="""Accepts Remote Access connections.<br>Available only if accept-control-connections is true.""",
    )
    accept_smart_update_connections: bool = Field(
        alias="accept-smart-update-connections",
        description="""Accepts SmartUpdate connections.""",
    )
    accept_outgoing_packets_originating_from_gw: bool = Field(
        alias="accept-outgoing-packets-originating-from-gw",
        description="""Accepts all packets from .connections that originate at the Check Point Security Gateway.""",
    )
    accept_outgoing_packets_originating_from_gw_position: str = Field(
        alias="accept-outgoing-packets-originating-from-gw-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-outgoing-packets-originating-from-gw is false.""",
    )
    accept_outgoing_packets_originating_from_connectra_gw: bool = Field(
        alias="accept-outgoing-packets-originating-from-connectra-gw",
        description="""Accepts outgoing packets originating from .Connectra gateway.<br>Available only if accept-outgoing-packets-originating-from-gw is false.""",
    )
    accept_outgoing_packets_to_cp_online_services: bool = Field(
        alias="accept-outgoing-packets-to-cp-online-services",
        description="""Allow Security Gateways to access Check Point online services. Supported for R80.10 Gateway and higher.<br>Available only if accept-outgoing-packets-originating-from-gw is false.""",
    )
    accept_outgoing_packets_to_cp_online_services_position: str = Field(
        alias="accept-outgoing-packets-to-cp-online-services-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-outgoing-packets-to-cp-online-services is true.""",
    )
    accept_domain_name_over_tcp: bool = Field(
        alias="accept-domain-name-over-tcp",
        description="""Accepts Domain Name (DNS) queries and replies over TCP, to allow downloading of the domain name-resolving tables used for zone transfers between servers. For clients, DNS over TCP is only used if the tables to be transferred are very large.""",
    )
    accept_domain_name_over_tcp_position: str = Field(
        alias="accept-domain-name-over-tcp-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-domain-name-over-tcp is true.""",
    )
    accept_domain_name_over_udp: bool = Field(
        alias="accept-domain-name-over-udp",
        description="""Accepts Domain Name (DNS) queries and replies over UDP.""",
    )
    accept_domain_name_over_udp_position: str = Field(
        alias="accept-domain-name-over-udp-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-domain-name-over-udp is true.""",
    )
    accept_dynamic_addr_modules_outgoing_internet_connections: bool = Field(
        alias="accept-dynamic-addr-modules-outgoing-internet-connections",
        description="""Accept Dynamic Address modules' outgoing internet connections.Accepts DHCP traffic for DAIP (Dynamically Assigned IP Address) gateways. In Small Office Appliance gateways, this rule allows outgoing DHCP, PPP, PPTP and L2TP Internet connections (regardless of whether it is or is not a DAIP gateway).""",
    )
    accept_icmp_requests: bool = Field(
        alias="accept-icmp-requests",
        description="""Accepts Internet Control Message Protocol messages.""",
    )
    accept_icmp_requests_position: str = Field(
        alias="accept-icmp-requests-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-icmp-requests is true.""",
    )
    accept_identity_awareness_control_connections: bool = Field(
        alias="accept-identity-awareness-control-connections",
        description="""Accepts traffic between Security Gateways in distributed environment configurations of Identity Awareness.""",
    )
    accept_identity_awareness_control_connections_position: str = Field(
        alias="accept-identity-awareness-control-connections-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-identity-awareness-control-connections is true.""",
    )
    accept_incoming_traffic_to_dhcp_and_dns_services_of_gws: bool = Field(
        alias="accept-incoming-traffic-to-dhcp-and-dns-services-of-gws",
        description="""Allows the Small Office Appliance gateway to provide DHCP relay, DHCP server and DNS proxy services regardless of the rule base.""",
    )
    accept_rip: bool = Field(
        alias="accept-rip",
        description="""Accepts Routing Information Protocol (RIP), using UDP on port 520.""",
    )
    accept_rip_position: str = Field(
        alias="accept-rip-position",
        description="""The position of the implied rules in the Rule Base.<br>Available only if accept-rip is true.""",
    )
    accept_vrrp_packets_originating_from_cluster_members: bool = Field(
        alias="accept-vrrp-packets-originating-from-cluster-members",
        description="""Selecting this option creates an implied rule in the security policy Rule Base that accepts VRRP inbound and outbound traffic to and from .the members of the cluster.""",
    )
    accept_web_and_ssh_connections_for_gw_administration: bool = Field(
        alias="accept-web-and-ssh-connections-for-gw-administration",
        description="""Accepts Web and SSH connections for Small Office Appliance gateways.""",
    )
    log_implied_rules: bool = Field(
        alias="log-implied-rules",
        description="""Produces log records for communications that match the implied rules that are generated in the Rule Base from .the properties defined in this window.""",
    )
    security_server: SecurityServerGlobalPropertiesRequest = Field(
        alias="security-server",
        description="""Control the welcome messages that users will see when logging in to servers behind Check Point Security Gateways.""",
    )
