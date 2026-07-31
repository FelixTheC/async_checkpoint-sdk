from pydantic import BaseModel, Field


class CarrierSecurityGlobalPropertiesReply(BaseModel):
    block_gtp_in_gtp: bool = Field(
        alias="block-gtp-in-gtp",
        description="""Prevents GTP packets from being encapsulated inside GTP tunnels. When this option is checked, such packets are dropped and logged.""",
    )
    enforce_gtp_anti_spoofing: bool = Field(
        alias="enforce-gtp-anti-spoofing",
        description="""verifies that G-PDUs are using the end user IP address that has been agreed upon in the PDP context activation process. When this option is checked, packets that do not use this IP address are dropped and logged.""",
    )
    produce_extended_logs_on_unmatched_pdus: bool = Field(
        alias="produce-extended-logs-on-unmatched-pdus",
        description="""logs GTP packets not matched by previous rules with Carrier Security's extended GTP-related log fields. These logs are brown and their Action attribute is empty. The default setting is checked.""",
    )
    produce_extended_logs_on_unmatched_pdus_position: str = Field(
        alias="produce-extended-logs-on-unmatched-pdus-position",
        description="""Choose to place this implicit rule Before Last or as the Last rule.<br>Available only if produce-extended-logs-on-unmatched-pdus is true.""",
    )
    protocol_violation_track_option: str = Field(
        alias="protocol-violation-track-option",
        description="""Set the appropriate track or alert option to be used when a protocol violation (malformed packet) is detected.""",
    )
    enable_g_pdu_seq_number_check_with_max_deviation: bool = Field(
        alias="enable-g-pdu-seq-number-check-with-max-deviation",
        description="""If set to false, sequence checking is not enforced and all out-of-sequence G-PDUs will be accepted.<br>To enhance performance, disable this extended integrity test.""",
    )
    g_pdu_seq_number_check_max_deviation: int = Field(
        alias="g-pdu-seq-number-check-max-deviation",
        description="""specifies that a G-PDU is accepted only if the difference between its sequence number and the expected sequence number is less than or equal to the allowed deviation.<br>Available only ifenable-g-pdu-seq-number-check-with-max-deviation is true.""",
    )
    verify_flow_labels: bool = Field(
        alias="verify-flow-labels",
        description="""See that each packet's flow label matches the flow labels defined by GTP signaling. This option is relevant for GTP version 0 only.<br>To enhance performance, disable this extended integrity test.""",
    )
    allow_ggsn_replies_from_multiple_interfaces: bool = Field(
        alias="allow-ggsn-replies-from-multiple-interfaces",
        description="""Allows GTP signaling replies from an IP address different from the IP address to which the requests are sent (Relevant only for gateways below R80).""",
    )
    enable_reverse_connections: bool = Field(
        alias="enable-reverse-connections",
        description="""Allows Carrier Security gateways to accept PDUs sent from the GGSN to the SGSN, on a previously established PDP context, even if these PDUs are sent over ports that do not match the ports of the established PDP context.""",
    )
    gtp_signaling_rate_limit_sampling_interval: int = Field(
        alias="gtp-signaling-rate-limit-sampling-interval",
        description="""Works in correlation with the property Enforce GTP Signal packet rate limit found in the Carrier Security window of the GSN network object. For example, with the rate limit sampling interval default of 1 second, and the network object enforced a GTP signal packet rate limit of the default 2048 PDU per second, sampling will occur one time per second, or 2048 signaling PDUs between two consecutive samplings.""",
    )
    one_gtp_echo_on_each_path_frequency: int = Field(
        alias="one-gtp-echo-on-each-path-frequency",
        description="""sets the number of GTP Echo exchanges per path allowed per configured time period. Echo requests exceeding this rate are dropped and logged. Setting the value to 0 disables the feature and allows an unlimited number of echo requests per path at any interval.""",
    )
    aggressive_aging: bool = Field(
        alias="aggressive-aging",
        description="""If true, enables configuring aggressive aging thresholds and time out value.""",
    )
    aggressive_timeout: int = Field(
        alias="aggressive-timeout",
        description="""Aggressive timeout. Available only if aggressive-aging is true.""",
    )
    memory_activation_threshold: int = Field(
        alias="memory-activation-threshold",
        description="""Memory activation threshold. Available only if aggressive-aging is true.""",
    )
    memory_deactivation_threshold: int = Field(
        alias="memory-deactivation-threshold",
        description="""Memory deactivation threshold. Available only if aggressive-aging is true.""",
    )
    tunnel_activation_threshold: int = Field(
        alias="tunnel-activation-threshold",
        description="""Tunnel activation threshold. Available only if aggressive-aging is true.""",
    )
    tunnel_deactivation_threshold: int = Field(
        alias="tunnel-deactivation-threshold",
        description="""Tunnel deactivation threshold. Available only if aggressive-aging is true.""",
    )
