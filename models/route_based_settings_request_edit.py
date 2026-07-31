from add import add
from participant_route_based_settings_request import (
    ParticipantRouteBasedSettingsRequest,
)
from pydantic import BaseModel, Field
from remove import remove
from route_based_advanced_settings_request import RouteBasedAdvancedSettingsRequest


class RouteBasedSettingsRequestEdit(BaseModel):
    add_automatic_routes: str = Field(
        alias="add-automatic-routes",
        description="""<html>The type of routes to use for the automatic Route-Based configuration.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    override_routes: (
        add | remove | ParticipantRouteBasedSettingsRequest | list[dict]
    ) = Field(
        alias="override-routes",
        description="""<html>Override automatic routing settings in a specific Security Gateway in this VPN Community.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    advanced: RouteBasedAdvancedSettingsRequest = Field(
        alias="advanced",
        description="""<html>Advanced settings<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
