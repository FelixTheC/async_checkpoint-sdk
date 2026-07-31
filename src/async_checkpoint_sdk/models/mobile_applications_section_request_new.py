from api_doc_rule_base_position_object_builder import ApiDocRuleBasePositionObjectBuilder
from pydantic import BaseModel, Field


class MobileApplicationsSectionRequestNew(BaseModel):
    position: int | str | ApiDocRuleBasePositionObjectBuilder = Field(
        alias="position", description="""Position in the rulebase."""
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
