from pydantic import BaseModel, Field


class VsxReconfigureGwRequest(BaseModel):
    ipv4_corexl_number: int = Field(
        alias="ipv4-corexl-number",
        description="""Number of IPv4 CoreXL Firewall instances on the target VSX Gateway.<br>Valid values:<br><ul><li>To configure CoreXL Firewall instances, enter an integer greater or equal to 2.</li><li>To disable CoreXL, enter 1.</li></ul>.""",
    )
    one_time_password: str = Field(
        alias="one-time-password",
        description="""A password required for establishing a Secure Internal Communication (SIC). Enter the same password you used during the First Time Configuration Wizard on the target VSX Gateway.""",
    )
    vsx_name: str = Field(alias="vsx-name", description="""Name of the VSX Gateway object.""")
