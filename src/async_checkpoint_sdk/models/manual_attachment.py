from .api_doc_rule_base_position_object_builder import (
    ApiDocRuleBasePositionObjectBuilder,
)
from .pydantic import BaseModel, Field


class ManualAttachment(BaseModel):
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
