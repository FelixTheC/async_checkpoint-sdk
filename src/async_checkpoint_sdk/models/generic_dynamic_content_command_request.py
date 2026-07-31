from .pydantic import BaseModel, Field
from .void import void


class GenericDynamicContentCommandRequest(BaseModel):
    handler: str = Field(alias="handler", description="""N/A""")
    parameters: void = Field(alias="parameters", description="""N/A""")
