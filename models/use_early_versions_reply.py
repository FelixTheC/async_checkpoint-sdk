from pydantic import BaseModel, Field


class UseEarlyVersionsReply(BaseModel):
    enabled: bool = Field(
        alias="enabled", description="""Use early versions compatibility mode."""
    )
    compatibility_mode: str = Field(
        alias="compatibility-mode", description="""Early versions compatibility mode."""
    )
