from .pydantic import BaseModel, Field


class TimeSettingsGlobalPropertiesReply(BaseModel):
    excessive_log_grace_period: int = Field(
        alias="excessive-log-grace-period",
        description="""Specifies the minimum amount of time (in seconds) between consecutive logs of similar packets. Two packets are considered similar if they have the same source address, source port, destination address, and destination port; and the same protocol was used. After the first packet, similar packets encountered in the grace period will be acted upon according to the security policy, but only the first packet generates a log entry or an alert. Any value from .0 to 90 seconds can be entered in this field.<br>Note: This option only applies for DROP rules with logging.""",
    )
    logs_resolving_timeout: int = Field(
        alias="logs-resolving-timeout",
        description="""Specifies the amount of time (in seconds), after which the log page is displayed without resolving names and while showing only IP addresses. Any value from .0 to 90 seconds can be entered in this field.""",
    )
    status_fetching_interval: int = Field(
        alias="status-fetching-interval",
        description="""Specifies the frequency at which the Security Management server queries the Check Point Security gateway, Check Point QoS and other gateways it manages for status information. Any value from .30 to 900 seconds can be entered in this field.""",
    )
    virtual_link_statistics_logging_interval: int = Field(
        alias="virtual-link-statistics-logging-interval",
        description="""Specifies the frequency (in seconds) with which Virtual Link statistics will be logged. This parameter is relevant only for Virtual Links defined with SmartView Monitor statistics enabled in the SLA Parameters tab of the Virtual Link window. Any value from .60 to 3600 seconds can be entered in this field.""",
    )
