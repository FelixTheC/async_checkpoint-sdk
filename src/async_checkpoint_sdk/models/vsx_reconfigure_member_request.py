from pydantic import BaseModel, Field


class VsxReconfigureMemberRequest(BaseModel):
    ipv4_corexl_number: int = Field(
        alias="ipv4-corexl-number",
        description="""Number of IPv4 CoreXL Firewall instances on the target VSX Cluster member.<br>Valid values:<br><ul><li>To configure CoreXL Firewall instances, enter an integer greater or equal to 2.</li><li>To disable CoreXL, enter 1.</li></ul>Important - The CoreXL configuration must be the same on all the cluster members.""",
    )
    member_uid: str = Field(
        alias="member-uid", description="""UID of the VSX Cluster member object."""
    )
    one_time_password: str = Field(
        alias="one-time-password",
        description="""A password required for establishing a Secure Internal Communication (SIC). Enter the same password you used during the First Time Configuration Wizard on the target VSX Cluster member.""",
    )
