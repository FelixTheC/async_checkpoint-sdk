from pydantic import BaseModel, Field


class SecurityGroupMemberInfoReply(BaseModel):
    appliance_model: str = Field(
        alias="appliance-model", description="""Appliance model of the Security Group Member."""
    )
    cpu_usage: int = Field(
        alias="cpu-usage", description="""CPU Usage (%) of the Security Group Member."""
    )
    disk_space_status: str = Field(
        alias="disk-space-status", description="""Disk space status of current member."""
    )
    filesystems: list[dict] = Field(
        alias="filesystems", description="""List of file systems to show per member."""
    )
    member_id: int = Field(
        alias="member-id", description="""ID of the Security Group Member on the Maestro Site."""
    )
    member_ip: str = Field(alias="member-ip", description="""Sync IP of current member.""")
    member_name: str = Field(
        alias="member-name", description="""Name of the Security Group Member."""
    )
    member_state: str = Field(
        alias="member-state", description="""State of the Security Group Member."""
    )
    memory_usage: int = Field(
        alias="memory-usage", description="""Memory usage (%) of the Security Group Member."""
    )
    serial_number: str = Field(
        alias="serial-number",
        description="""Appliance serial number of the Security Group Member.""",
    )
    site_id: int = Field(alias="site-id", description="""ID of the Maestro Site.""")
    throughput: int = Field(
        alias="throughput", description="""Total throughput of the Security Group Member."""
    )
    version: str = Field(
        alias="version", description="""Software version installed on the Security Group Member."""
    )
