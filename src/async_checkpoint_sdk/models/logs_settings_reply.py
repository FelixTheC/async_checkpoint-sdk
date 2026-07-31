from .pydantic import BaseModel, Field


class LogsSettingsReply(BaseModel):
    alert_when_free_disk_space_below: bool = Field(
        alias="alert-when-free-disk-space-below",
        description="""Alert when free disk space is below threshold enabled.""",
    )
    alert_when_free_disk_space_below_metrics: str = Field(
        alias="alert-when-free-disk-space-below-metrics",
        description="""Alert when free disk space below metrics.""",
    )
    alert_when_free_disk_space_below_threshold: int = Field(
        alias="alert-when-free-disk-space-below-threshold",
        description="""Alert when free disk space below threshold.""",
    )
    alert_when_free_disk_space_below_type: str = Field(
        alias="alert-when-free-disk-space-below-type",
        description="""Alert when free disk space below type.""",
    )
    before_delete_keep_logs_from_the_last_days: bool = Field(
        alias="before-delete-keep-logs-from-the-last-days",
        description="""Before delete keep logs from .the last days enabled.""",
    )
    before_delete_keep_logs_from_the_last_days_threshold: int = Field(
        alias="before-delete-keep-logs-from-the-last-days-threshold",
        description="""Before delete keep logs from .the last days threshold.""",
    )
    before_delete_run_script: bool = Field(
        alias="before-delete-run-script",
        description="""Before delete run script enabled.""",
    )
    before_delete_run_script_command: str = Field(
        alias="before-delete-run-script-command",
        description="""Before delete run script command.""",
    )
    delete_index_files_older_than_days: bool = Field(
        alias="delete-index-files-older-than-days",
        description="""Delete index files older than days enabled.""",
    )
    delete_index_files_older_than_days_threshold: int = Field(
        alias="delete-index-files-older-than-days-threshold",
        description="""Delete index files older than days threshold.""",
    )
    delete_index_files_when_index_size_above: bool = Field(
        alias="delete-index-files-when-index-size-above",
        description="""Delete index files when index size above enabled.""",
    )
    delete_index_files_when_index_size_above_metrics: str = Field(
        alias="delete-index-files-when-index-size-above-metrics",
        description="""Delete index files when index size above metrics.""",
    )
    delete_index_files_when_index_size_above_threshold: int = Field(
        alias="delete-index-files-when-index-size-above-threshold",
        description="""Delete index files when index size above threshold.""",
    )
    delete_when_free_disk_space_below: bool = Field(
        alias="delete-when-free-disk-space-below",
        description="""Delete when free disk space below enabled.""",
    )
    delete_when_free_disk_space_below_metrics: str = Field(
        alias="delete-when-free-disk-space-below-metrics",
        description="""Delete when free disk space below metrics.""",
    )
    delete_when_free_disk_space_below_threshold: int = Field(
        alias="delete-when-free-disk-space-below-threshold",
        description="""Delete when free disk space below threshold.""",
    )
    detect_new_citrix_ica_application_names: bool = Field(
        alias="detect-new-citrix-ica-application-names",
        description="""Detect new Citrix ICA application names enabled.""",
    )
    distribute_logs_between_all_active_servers: bool = Field(
        alias="distribute-logs-between-all-active-servers",
        description="""Distribute logs between all active servers.""",
    )
    forward_logs_to_log_server: bool = Field(
        alias="forward-logs-to-log-server",
        description="""Forward logs to log server enabled.""",
    )
    forward_logs_to_log_server_name: str = Field(
        alias="forward-logs-to-log-server-name",
        description="""Forward logs to log server name.""",
    )
    forward_logs_to_log_server_schedule_name: str = Field(
        alias="forward-logs-to-log-server-schedule-name",
        description="""Forward logs to log server schedule name.""",
    )
    perform_log_rotate_before_log_forwarding: bool = Field(
        alias="perform-log-rotate-before-log-forwarding",
        description="""Perform log rotate before log forwarding enabled.""",
    )
    reject_connections_when_free_disk_space_below_threshold: bool = Field(
        alias="reject-connections-when-free-disk-space-below-threshold",
        description="""Reject connections when free disk space below threshold enabled.""",
    )
    reserve_for_packet_capture_metrics: str = Field(
        alias="reserve-for-packet-capture-metrics",
        description="""Reserve for packet capture metrics.""",
    )
    reserve_for_packet_capture_threshold: int = Field(
        alias="reserve-for-packet-capture-threshold",
        description="""Reserve for packet capture threshold.""",
    )
    rotate_log_by_file_size: bool = Field(
        alias="rotate-log-by-file-size",
        description="""Rotate log by file size enabled.""",
    )
    rotate_log_file_size_threshold: int = Field(
        alias="rotate-log-file-size-threshold",
        description="""Log file size threshold.""",
    )
    rotate_log_on_schedule: bool = Field(
        alias="rotate-log-on-schedule",
        description="""Rotate log on schedule enabled.""",
    )
    rotate_log_schedule_name: str = Field(
        alias="rotate-log-schedule-name", description="""Rotate log schedule name."""
    )
    stop_logging_when_free_disk_space_below: bool = Field(
        alias="stop-logging-when-free-disk-space-below",
        description="""Stop logging when free disk space below enabled.""",
    )
    stop_logging_when_free_disk_space_below_metrics: str = Field(
        alias="stop-logging-when-free-disk-space-below-metrics",
        description="""Stop logging when free disk space below metrics.""",
    )
    stop_logging_when_free_disk_space_below_threshold: int = Field(
        alias="stop-logging-when-free-disk-space-below-threshold",
        description="""Stop logging when free disk space below threshold.""",
    )
    turn_on_qos_logging: bool = Field(
        alias="turn-on-qos-logging", description="""Turn on QoS Logging enabled."""
    )
    update_account_log_every: int = Field(
        alias="update-account-log-every",
        description="""Update account log in every amount of seconds.""",
    )
