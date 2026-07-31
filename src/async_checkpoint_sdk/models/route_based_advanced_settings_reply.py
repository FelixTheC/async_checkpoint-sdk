from pydantic import BaseModel, Field


class RouteBasedAdvancedSettingsReply(BaseModel):
    bfd: bool = Field(
        alias="bfd",
        description="""<html>Indicates whether to enable Bidirectional Forwarding Detection.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    graceful_restart: bool = Field(
        alias="graceful-restart",
        description="""<html>Indicates whether to enable Graceful Restart in the applicable Dynamic Routing protocols.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
