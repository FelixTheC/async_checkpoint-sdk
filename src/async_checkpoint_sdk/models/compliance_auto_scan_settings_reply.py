from pydantic import BaseModel, Field


class ComplianceAutoScanSettingsReply(BaseModel):
    scan_day: str = Field(
        alias="scan-day",
        description="""Schedules the day of the week for the Compliance scan. The default is every_day.""",
    )
    scan_time: str = Field(
        alias="scan-time",
        description="""Schedules the time of the day for the Compliance scan in format: HH:mm:ss.""",
    )
    scheduled_scan_on: bool = Field(
        alias="scheduled-scan-on",
        description="""Determines whether to enable the scheduled scan.""",
    )
