from .fw_rule_condition_type_reply import FwRuleConditionTypeReply
from .grc_fw_rule_object_reply import GrcFwRuleObjectReply
from .pydantic import BaseModel, Field


class GrcFwRuleReply(BaseModel):
    action: GrcFwRuleObjectReply = Field(alias="action", description="""User-defined actions.""")
    comment: FwRuleConditionTypeReply = Field(
        alias="comment", description="""User-defined comment."""
    )
    destination: GrcFwRuleObjectReply = Field(
        alias="destination", description="""User-defined destination objects."""
    )
    hit_count: GrcFwRuleObjectReply = Field(
        alias="hit-count", description="""User-defined hit count value."""
    )
    install_on: GrcFwRuleObjectReply = Field(
        alias="install-on", description="""User-defined Install On objects."""
    )
    name: FwRuleConditionTypeReply = Field(alias="name", description="""User-defined name.""")
    services_and_applications: GrcFwRuleObjectReply = Field(
        alias="services-and-applications",
        description="""User-defined service and application objects.""",
    )
    source: GrcFwRuleObjectReply = Field(
        alias="source", description="""User-defined source objects."""
    )
    time: GrcFwRuleObjectReply = Field(alias="time", description="""User-defined time.""")
    track: GrcFwRuleObjectReply = Field(
        alias="track", description="""User-defined track actions."""
    )
    vpn: GrcFwRuleObjectReply = Field(alias="vpn", description="""User-defined VPN objects.""")
