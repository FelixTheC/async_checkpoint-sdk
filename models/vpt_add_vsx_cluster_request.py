from pydantic import BaseModel, Field


class VptAddVsxClusterRequest(BaseModel):
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
