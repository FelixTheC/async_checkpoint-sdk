from pydantic import BaseModel, Field


class VpnDirectionalRequest(BaseModel):
    source: str = Field(alias="from", description="""From community name or UID.""")
    to: str = Field(alias="to", description="""To community name or UID.""")
