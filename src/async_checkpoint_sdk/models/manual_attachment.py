from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class ManualAttachment(BaseModel):
    layer: str = Field(
        alias="layer",
        description="""The layer of the threat rule to which the group is to be attached.""",
    )
    uid: str = Field(
        alias="uid",
        description="""The uid of the threat rule to which the group is to be attached.""",
    )
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
