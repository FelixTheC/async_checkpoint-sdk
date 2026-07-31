from .pydantic import BaseModel, Field


class CommWithServerBehindNatSettingsReply(BaseModel):
    override_profile: bool = Field(
        alias="override-profile",
        description="""Whether to override the Server (Check Point Host) object configuration.""",
    )
    value: str = Field(
        alias="value",
        description="""according-to-topology: Use the original or translated IP address of the server based on the Topology of Security Gateway interfaces.<br>original-ip-only: Use only the original IP address of the server<br>translated-ip-only: Use only the translated IP address of the server.""",
    )
