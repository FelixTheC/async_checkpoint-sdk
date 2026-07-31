from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class RuleBatchSupportedObjectForAdd(BaseModel):
    layer: str = Field(alias="layer", description="""Layer name or uid.""")
    type: str = Field(
        alias="type",
        description="""Type of rules to be created. <br>Only types from above are supported.""",
    )
    first_position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="first-position", description="""First rule position."""
    )
    list: list[dict] = Field(
        alias="list",
        description="""List of rules from the same type to be created on the same layer. <br>Use the add API reference documentation for a single rule command to find the expected fields for the request. <br>For example: to add access-rules, use the add-access-rule command found in the API reference documentation (under Access Control & NAT). <br>Note: set-if-exists, ignore-errors, ignore-warnings and details-level options are not supported when adding a batch of rules.""",
    )
