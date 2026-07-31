from .pydantic import BaseModel, Field


class IpsAdditionalPropertiesReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    values: list[dict] = Field(alias="values", description="""N/A""")
