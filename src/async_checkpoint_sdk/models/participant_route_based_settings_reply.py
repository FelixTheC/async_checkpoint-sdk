from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .exported_routes_reply import ExportedRoutesReply
from .pydantic import BaseModel, Field


class ParticipantRouteBasedSettingsReply(BaseModel):
    gateway: ApiObjectStandardIdentifier = Field(
        alias="gateway",
        description="""<html>Name of the Security Gateway object in which to override the automatic routing settings.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    auto_config: bool = Field(
        alias="auto-config",
        description="""<html>Indicates whether to configure the routing settings automatically for the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    mode: str = Field(
        alias="mode",
        description="""<html>Specifies how to export routes from .the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    exported_routes: ExportedRoutesReply = Field(
        alias="exported-routes",
        description="""<html>Exported Routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
