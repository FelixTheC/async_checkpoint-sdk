from pydantic import BaseModel, Field


class SmbLogsSettingsRequest(BaseModel):
    alert_when_queue_is_full: bool = Field(
        alias="alert-when-queue-is-full", description="""Alert when queue is full enabled."""
    )
    alert_when_queue_is_full_type: str = Field(
        alias="alert-when-queue-is-full-type", description="""Alert when queue is full type."""
    )
    detect_new_citrix_ica_application_names: bool = Field(
        alias="detect-new-citrix-ica-application-names",
        description="""Detect new citrix ica application names enabled.""",
    )
    stop_logging_when_queue_reaches_maximal_capacity: bool = Field(
        alias="stop-logging-when-queue-reaches-maximal-capacity",
        description="""Stop logging when queue reaches maximal capacity enabled.""",
    )
    stop_logging_when_queue_reaches_maximal_capacity_threshold: int = Field(
        alias="stop-logging-when-queue-reaches-maximal-capacity-threshold",
        description="""Stop logging when queue reaches maximal capacity threshold.""",
    )
    turn_on_qos_logging: bool = Field(
        alias="turn-on-qos-logging", description="""Turn on qos logging enabled."""
    )
    update_account_log_every: int = Field(
        alias="update-account-log-every",
        description="""Update account log in every amount of seconds.""",
    )
