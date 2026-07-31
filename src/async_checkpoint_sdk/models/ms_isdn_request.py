from pydantic import BaseModel, Field


class MsIsdnRequest(BaseModel):
    enable: bool = Field(alias="enable", description="""""")
    ms_isdn: str = Field(alias="ms-isdn", description="""The MS-ISDN.""")
