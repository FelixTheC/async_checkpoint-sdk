from pydantic import BaseModel, Field


class UseEarlyVersionsRequest(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Use early versions compatibility mode."""
    )
    compatibility_mode: str = Field(
        alias="compatibility-mode", description="""Early versions compatibility mode."""
    )
