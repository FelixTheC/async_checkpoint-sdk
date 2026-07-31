from pydantic import BaseModel, Field


class AutoCompleteRequest(BaseModel):
    cursor_position: int = Field(alias="cursor-position", description="""N/A""")
    prefix: str = Field(alias="prefix", description="""N/A""")
