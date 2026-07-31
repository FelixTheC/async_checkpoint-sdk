from .pydantic import BaseModel, Field


class ReplaceInRulesRequest(BaseModel):
    layer: str = Field(alias="layer", description="""The UID of the layer the rule belongs to.""")
    package: str = Field(
        alias="package",
        description="""The UID of the policy package where the rule is defined.""",
    )
    replacement_field_path: str = Field(
        alias="replacement-field-path",
        description="""Path of the field in the rule where the object should be replaced.""",
    )
