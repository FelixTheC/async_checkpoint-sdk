from pydantic import BaseModel, Field
from route_based_advanced_settings_reply import RouteBasedAdvancedSettingsReply


class RouteBasedSettingsReply(BaseModel):
    add_automatic_routes: str = Field(
        alias="add-automatic-routes",
        description="""<html>The type of routes to use for the automatic Route-Based configuration.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    override_routes: list[dict] = Field(
        alias="override-routes",
        description="""<html>Override automatic routing settings in a specific Security Gateway in this VPN Community.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    advanced: RouteBasedAdvancedSettingsReply = Field(
        alias="advanced",
        description="""<html>Advanced settings<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
