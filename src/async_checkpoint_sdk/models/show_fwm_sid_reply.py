from .pydantic import BaseModel, Field


class ShowFwmSidReply(BaseModel):
    fwm_sid: str = Field(alias="fwm-sid", description="""N/A""")
