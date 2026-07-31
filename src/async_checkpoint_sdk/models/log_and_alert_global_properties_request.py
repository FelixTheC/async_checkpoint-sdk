from alerts_global_properties_request import AlertsGlobalPropertiesRequest
from pydantic import BaseModel, Field
from time_settings_global_properties_request import TimeSettingsGlobalPropertiesRequest


class LogAndAlertGlobalPropertiesRequest(BaseModel):
    administrative_notifications: str = Field(
        alias="administrative-notifications",
        description="""Administrative notifications specifies the action to be taken when an administrative event (for example, when a certificate is about to expire) occurs.""",
    )
    connection_matched_by_sam: str = Field(
        alias="connection-matched-by-sam",
        description="""Connection matched by SAM specifies the action to be taken when a connection is blocked by SAM (Suspicious Activities Monitoring).""",
    )
    dynamic_object_resolution_failure: str = Field(
        alias="dynamic-object-resolution-failure",
        description="""Dynamic object resolution failure specifies the action to be taken when a dynamic object cannot be resolved.""",
    )
    ip_options_drop: str = Field(
        alias="ip-options-drop",
        description="""IP Options drop specifies the action to take when a packet with IP Options is encountered. The Check Point Security Gateway always drops these packets, but you can log them or issue an alert.""",
    )
    packet_is_incorrectly_tagged: str = Field(
        alias="packet-is-incorrectly-tagged", description="""Packet is incorrectly tagged."""
    )
    packet_tagging_brute_force_attack: str = Field(
        alias="packet-tagging-brute-force-attack",
        description="""Packet tagging brute force attack.""",
    )
    sla_violation: str = Field(
        alias="sla-violation",
        description="""SLA violation specifies the action to be taken when an SLA violation occurs, as defined in the Virtual Links window.""",
    )
    vpn_conf_and_key_exchange_errors: str = Field(
        alias="vpn-conf-and-key-exchange-errors",
        description="""VPN configuration & key exchange errors specifies the action to be taken when logging configuration or key exchange errors occur, for example, when attempting to establish encrypted communication with a network object inside the same encryption domain.""",
    )
    vpn_packet_handling_error: str = Field(
        alias="vpn-packet-handling-error",
        description="""VPN packet handling errors specifies the action to be taken when encryption or decryption errors occurs. A log entry contains the action performed (Drop or Reject) and a short description of the error cause, for example, scheme or method mismatch.""",
    )
    vpn_successful_key_exchange: str = Field(
        alias="vpn-successful-key-exchange",
        description="""VPN successful key exchange specifies the action to be taken when VPN keys are successfully exchanged.""",
    )
    log_every_authenticated_http_connection: bool = Field(
        alias="log-every-authenticated-http-connection",
        description="""Log every authenticated HTTP connection specifies that a log entry should be generated for every authenticated HTTP connection.""",
    )
    log_traffic: str = Field(
        alias="log-traffic", description="""Log Traffic specifies whether or not to log traffic."""
    )
    alerts: AlertsGlobalPropertiesRequest = Field(
        alias="alerts",
        description="""Define the behavior of alert logs and the type of alert used for System Alert logs.""",
    )
    time_settings: TimeSettingsGlobalPropertiesRequest = Field(
        alias="time-settings",
        description="""Configure the time settings associated with system-wide logging and alerting parameters.""",
    )
