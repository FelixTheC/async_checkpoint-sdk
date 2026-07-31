from add import add
from pydantic import BaseModel, Field
from remove import remove


class StatefulInspectionGlobalPropertiesRequest(BaseModel):
    tcp_start_timeout: int = Field(
        alias="tcp-start-timeout",
        description="""A TCP connection will be timed out if the interval between the arrival of the first packet and establishment of the connection (TCP three-way handshake) exceeds TCP start timeout seconds.""",
    )
    tcp_session_timeout: int = Field(
        alias="tcp-session-timeout",
        description="""The length of time (in seconds) an idle connection will remain in the Security Gateway connections table.""",
    )
    tcp_end_timeout: int = Field(
        alias="tcp-end-timeout",
        description="""A TCP connection will only terminate TCP end timeout seconds after two FIN packets (one in each direction: client-to-server, and server-to-client) or an RST packet. When a TCP connection ends (FIN packets sent or connection reset) the Check Point Security Gateway will keep the connection in the connections table for another TCP end timeout seconds, to allow for stray ACKs of the connection that arrive late.""",
    )
    tcp_end_timeout_r8020_gw_and_above: int = Field(
        alias="tcp-end-timeout-r8020-gw-and-above",
        description="""A TCP connection will only terminate TCP end timeout seconds after two FIN packets (one in each direction: client-to-server, and server-to-client) or an RST packet. When a TCP connection ends (FIN packets sent or connection reset) the Check Point Security Gateway will keep the connection in the connections table for another TCP end timeout seconds, to allow for stray ACKs of the connection that arrive late.""",
    )
    udp_virtual_session_timeout: int = Field(
        alias="udp-virtual-session-timeout",
        description="""Specifies the amount of time (in seconds) a UDP reply channel may remain open without any packets being returned.""",
    )
    icmp_virtual_session_timeout: int = Field(
        alias="icmp-virtual-session-timeout",
        description="""An ICMP virtual session will be considered to have timed out after this time period (in seconds).""",
    )
    other_ip_protocols_virtual_session_timeout: int = Field(
        alias="other-ip-protocols-virtual-session-timeout",
        description="""A virtual session of services which are not explicitly configured here will be considered to have timed out after this time period (in seconds).""",
    )
    sctp_start_timeout: int = Field(
        alias="sctp-start-timeout",
        description="""SCTP connections will be timed out if the interval between the arrival of the first packet and establishment of the connection exceeds this value (in seconds).""",
    )
    sctp_session_timeout: int = Field(
        alias="sctp-session-timeout",
        description="""Time (in seconds) an idle connection will remain in the Security Gateway connections table.""",
    )
    sctp_end_timeout: int = Field(
        alias="sctp-end-timeout",
        description="""SCTP connections end after this number of seconds, after the connection ends or is reset, to allow for stray ACKs of the connection that arrive late.""",
    )
    accept_stateful_udp_replies_for_unknown_services: bool = Field(
        alias="accept-stateful-udp-replies-for-unknown-services",
        description="""Specifies if UDP replies are to be accepted for unknown services.""",
    )
    accept_stateful_icmp_errors: bool = Field(
        alias="accept-stateful-icmp-errors",
        description="""Accept ICMP error packets which refer to another non-ICMP connection (for example, to an ongoing TCP or UDP connection) that was accepted by the Rule Base.""",
    )
    accept_stateful_icmp_replies: bool = Field(
        alias="accept-stateful-icmp-replies",
        description="""Accept ICMP reply packets for ICMP requests that were accepted by the Rule Base.""",
    )
    accept_stateful_other_ip_protocols_replies_for_unknown_services: bool = Field(
        alias="accept-stateful-other-ip-protocols-replies-for-unknown-services",
        description="""Accept reply packets for other undefined services (that is, services which are not one of the following: TCP, UDP, ICMP).""",
    )
    drop_out_of_state_tcp_packets: bool = Field(
        alias="drop-out-of-state-tcp-packets",
        description="""Drop TCP packets which are not consistent with the current state of the connection.""",
    )
    log_on_drop_out_of_state_tcp_packets: bool = Field(
        alias="log-on-drop-out-of-state-tcp-packets",
        description="""Generates a log entry when these out of state TCP packets are dropped.<br>Available only if drop-out-of-state-tcp-packets is true.""",
    )
    tcp_out_of_state_drop_exceptions: add | remove | str | list[str] = Field(
        alias="tcp-out-of-state-drop-exceptions",
        description="""Name or uid of the gateways and clusters for which Out of State packets are allowed.""",
    )
    drop_out_of_state_icmp_packets: bool = Field(
        alias="drop-out-of-state-icmp-packets",
        description="""Drop ICMP packets which are not consistent with the current state of the connection.""",
    )
    log_on_drop_out_of_state_icmp_packets: bool = Field(
        alias="log-on-drop-out-of-state-icmp-packets",
        description="""Generates a log entry when these out of state ICMP packets are dropped.<br>Available only if drop-out-of-state-icmp-packets is true.""",
    )
    drop_out_of_state_sctp_packets: bool = Field(
        alias="drop-out-of-state-sctp-packets",
        description="""Drop SCTP packets which are not consistent with the current state of the connection.""",
    )
    log_on_drop_out_of_state_sctp_packets: bool = Field(
        alias="log-on-drop-out-of-state-sctp-packets",
        description="""Generates a log entry when these out of state SCTP packets are dropped.<br>Available only if drop-out-of-state-sctp-packets is true.""",
    )
