from pydantic import BaseModel, Field


class VptAddVsxGwRequest(BaseModel):
    ipv4_address: str = Field(
        alias="ipv4-address",
        description="""Main IPv4 Address of the VSX Gateway or Cluster object.<br/>Optional if main IPv6 Address is defined.""",
    )
    ipv6_address: str = Field(
        alias="ipv6-address",
        description="""Main IPv6 Address of the VSX Gateway or Cluster object.<br/>Optional if main IPv4 Address is defined.""",
    )
    sic_otp: str = Field(
        alias="sic-otp",
        description="""SIC one-time-password of the VSX Gateway or Cluster member.<br/>Password must be between 4-127 characters in length.""",
    )
    version: str = Field(
        alias="version", description="""Version of the VSX Gateway or Cluster object."""
    )
    vsx_name: str = Field(
        alias="vsx-name", description="""Name of the VSX Gateway or Cluster object."""
    )
    rule_drop: str = Field(
        alias="rule-drop",
        description="""Add a default drop rule to the VSX Gateway or Cluster initial policy.""",
    )
    rule_https: str = Field(
        alias="rule-https",
        description="""Add a rule to allow HTTPS traffic to the VSX Gateway or Cluster initial policy.""",
    )
    rule_ping: str = Field(
        alias="rule-ping",
        description="""Add a rule to allow ping traffic to the VSX Gateway or Cluster initial policy.""",
    )
    rule_ping6: str = Field(
        alias="rule-ping6",
        description="""Add a rule to allow ping6 traffic to the VSX Gateway or Cluster initial policy.""",
    )
    rule_snmp: str = Field(
        alias="rule-snmp",
        description="""Add a rule to allow SNMP traffic to the VSX Gateway or Cluster initial policy.""",
    )
    rule_ssh: str = Field(
        alias="rule-ssh",
        description="""Add a rule to allow SSH traffic to the VSX Gateway or Cluster initial policy.""",
    )
