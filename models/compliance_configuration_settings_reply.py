from api_domain_identifier import ApiDomainIdentifier
from compliance_auto_scan_settings_reply import ComplianceAutoScanSettingsReply
from pydantic import BaseModel, Field


class ComplianceConfigurationSettingsReply(BaseModel):
    automatic_scan_scheduler: ComplianceAutoScanSettingsReply = Field(
        alias="automatic-scan-scheduler",
        description="""Schedule for an automatic full Compliance blade scan.""",
    )
    enable_email_alerts: bool = Field(
        alias="enable-email-alerts",
        description="""Enables or disables sending email alerts to SmartEvent (only for alerts).""",
    )
    enable_smart_event_logs: bool = Field(
        alias="enable-smart-event-logs",
        description="""Enables or disables sending logs to SmartEvent.""",
    )
    initialize_best_practices: bool = Field(
        alias="initialize-best-practices",
        description="""Determines if this is the first scan.
If 'true', the next Compliance Scan runs as if it is the first scan. This creates all the default Best Practices again.
After the first scan completes, the value of this parameter is automatically set to 'false'.""",
    )
    partial_scan_delay: int = Field(
        alias="partial-scan-delay",
        description="""If the value is < 0, then the partial run does not start.
If the value > 0, then after you publish the session, partial scan is delayed for the specified number second.
If the value = 0, then the partial scan starts immediately after you publish the session.""",
    )
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
