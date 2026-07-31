from .pydantic import BaseModel, Field


class GwProxyCmdRequest(BaseModel):
    other_parameter: str = Field(
        alias="other-parameter",
        description="""Other input parameters that gateway needs it.""",
    )
