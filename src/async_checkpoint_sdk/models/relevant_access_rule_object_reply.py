from pydantic import BaseModel, Field


class RelevantAccessRuleObjectReply(BaseModel):
    enabled: bool = Field(
        alias="enabled",
        description="""Shows if the Compliance scan is enabled or not for this object.""",
    )
    layer_name: str = Field(
        alias="layer-name", description="""The name of the relevant policy layer."""
    )
    layer_uid: str = Field(
        alias="layer-uid", description="""The UID of the relevant policy layer."""
    )
    policy_name: str = Field(
        alias="policy-name", description="""The name of the relevant policy."""
    )
    rule_indexes: str = Field(
        alias="rule-indexes",
        description="""Comma-separated indexes of the relevant rules in the relevant policy and policy layer.""",
    )
    status: str = Field(alias="status", description="""The status of the relevant object.""")
