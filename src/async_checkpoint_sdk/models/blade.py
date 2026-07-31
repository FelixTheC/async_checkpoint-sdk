from .pydantic import BaseModel, Field


class Blade(BaseModel):
    default: bool = Field(alias="default", description="""N/A""")
    name: str = Field(alias="name", description="""N/A""")
    readonly: bool = Field(alias="readonly", description="""N/A""")
