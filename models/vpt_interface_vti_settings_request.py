from pydantic import BaseModel, Field


class VptInterfaceVtiSettingsRequest(BaseModel):
    tunnel_id: str = Field(
        alias="tunnel-id",
        description="""Optional unique Tunnel ID.<br/>Automatically assigned by the system if empty.""",
    )
