from .pydantic import BaseModel, Field


class IEntityInRulebase(BaseModel):
    type: str = Field(alias="type", description="""Rules type.""")
