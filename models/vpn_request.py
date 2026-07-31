from pydantic import BaseModel, Field


class VpnRequest(BaseModel):
    community: list[str] = Field(
        alias="community", description="""List of community name or UID."""
    )
