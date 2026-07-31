from exported_routes_request_new import ExportedRoutesRequestNew
from pydantic import BaseModel, Field


class ParticipantRouteBasedSettingsRequest(BaseModel):
    auto_config: bool = Field(
        alias="auto-config",
        description="""<html>Indicates whether to configure the routing settings automatically for the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    mode: str = Field(
        alias="mode",
        description="""<html>Specifies how to export routes from the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    exported_routes: ExportedRoutesRequestNew = Field(
        alias="exported-routes",
        description="""<html>Exported Routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
