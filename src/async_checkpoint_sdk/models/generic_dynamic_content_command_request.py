from pydantic import BaseModel, Field
from void import Void


class GenericDynamicContentCommandRequest(BaseModel):
    handler: str = Field(alias="handler", description="""N/A""")
    parameters: Void = Field(alias="parameters", description="""N/A""")
