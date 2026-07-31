from pydantic import BaseModel, Field


class ComplianceAutoScanSettingsRequest(BaseModel):
    scan_day: str = Field(
        alias="scan-day",
        description="""The scheduled day of the week for the Compliance scan. The default value is 'every_day'.""",
    )
    scan_time: str = Field(
        alias="scan-time",
        description="""The scheduled time of day for the Compliance scanin format: HH:mm:ss.
 The default value is '23:59:59'.""",
    )
    scheduled_scan_on: bool = Field(
        alias="scheduled-scan-on",
        description="""Enables or disables the scheduled scan. The default value is 'true'.""",
    )
