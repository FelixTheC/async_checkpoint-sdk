from pydantic import BaseModel, Field


class GrcFwRuleObjectReply(BaseModel):
    negate: bool = Field(alias="negate", description="""Shows if the rule is negated.""")
    reference_objects: list[dict] = Field(
        alias="reference-objects", description="""The reference objects."""
    )
