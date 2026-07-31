from ips_top_cpu_consuming_protections_settings_request import (
    IpsTopCpuConsumingProtectionsSettingsRequest,
)
from pydantic import BaseModel, Field


class IpsSettingsRequestEdit(BaseModel):
    bypass_all_under_load: bool = Field(
        alias="bypass-all-under-load",
        description="""Disable/enable all IPS protections until CPU and memory levels are back to normal.""",
    )
    bypass_track_method: str = Field(
        alias="bypass-track-method",
        description="""Track options when all IPS protections are disabled until CPU/memory levels are back to normal.""",
    )
    top_cpu_consuming_protections: IpsTopCpuConsumingProtectionsSettingsRequest = Field(
        alias="top-cpu-consuming-protections",
        description="""Provides a way to reduce CPU levels on machines under load by disabling the top CPU consuming IPS protections.""",
    )
    activation_mode: str = Field(
        alias="activation-mode",
        description="""Defines whether the IPS blade operates in Detect Only mode or enforces the configured IPS Policy.""",
    )
    cpu_usage_low_threshold: int = Field(
        alias="cpu-usage-low-threshold",
        description="""CPU usage low threshold percentage (1-99).""",
    )
    cpu_usage_high_threshold: int = Field(
        alias="cpu-usage-high-threshold",
        description="""CPU usage high threshold percentage (1-99).""",
    )
    memory_usage_low_threshold: int = Field(
        alias="memory-usage-low-threshold",
        description="""Memory usage low threshold percentage (1-99).""",
    )
    memory_usage_high_threshold: int = Field(
        alias="memory-usage-high-threshold",
        description="""Memory usage high threshold percentage (1-99).""",
    )
    send_threat_cloud_info: bool = Field(
        alias="send-threat-cloud-info",
        description="""Help improve Check Point Threat Prevention product by sending anonymous information.""",
    )
