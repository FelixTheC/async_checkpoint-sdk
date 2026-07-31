from pydantic import BaseModel, Field


class GatewayGlobalUseRequestShow(BaseModel):
    target: str = Field(
        alias="target",
        description="""On what target to execute this command. Target may be identified by its object name, or object unique identifier.""",
    )
