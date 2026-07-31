from .pydantic import BaseModel, Field


class AccessPointNameRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    apn: str = Field(
        alias="apn",
        description="""The Access Point Name object identified by Name or UID.""",
    )
