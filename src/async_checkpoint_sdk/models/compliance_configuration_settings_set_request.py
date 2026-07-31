from compliance_auto_scan_settings_request import ComplianceAutoScanSettingsRequest
from pydantic import BaseModel, Field


class ComplianceConfigurationSettingsSetRequest(BaseModel):
    automatic_scan_scheduler: ComplianceAutoScanSettingsRequest = Field(
        alias="automatic-scan-scheduler",
        description="""Schedule for an automatic full Compliance scan.""",
    )
    enable_email_alerts: bool = Field(
        alias="enable-email-alerts",
        description="""Enables or disables sending email alerts to SmartEvent (only for alerts).
The default value is 'true'.""",
    )
    enable_smart_event_logs: bool = Field(
        alias="enable-smart-event-logs",
        description="""Enables or disables sending logs to SmartEvent.
The default value is 'true'.""",
    )
    initialize_best_practices: bool = Field(
        alias="initialize-best-practices",
        description="""If 'true', creates all the default Best Practices again.
After the first scan completes, the value of this parameter is automatically set to 'false'.
The default value is 'true' for initial setup and 'false' after first scan.""",
    )
    partial_scan_delay: int = Field(
        alias="partial-scan-delay",
        description="""Controls when the partial scan starts after publishing a session. The partial scan checks only the relevant firewall best practices.
If the value is < 0, the partial scan is disabled.
If the value is 0, the partial scan starts immediately after publishing.
If the value is > 0, the partial scan is delayed by the specified number of seconds after publishing.
The default value is '0'.""",
    )
