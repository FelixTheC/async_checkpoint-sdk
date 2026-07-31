from .pydantic import BaseModel, Field
from .replace_in_rules_request import ReplaceInRulesRequest


class WhereUsedReplaceObjectRequest(BaseModel):
    replace_with: str = Field(
        alias="replace-with",
        description="""The object that will replace the old object identified by name or UID.""",
    )
    replace_in_rules: ReplaceInRulesRequest | list[dict] = Field(
        alias="replace-in-rules",
        description="""One or more rule references where the object will be replaced (used only if replaceScope includes rules).""",
    )
    replace_in_objects: str | list[str] = Field(
        alias="replace-in-objects",
        description="""One or more object UIDs where the object will be replaced (used only if replaceScope includes objects).""",
    )
