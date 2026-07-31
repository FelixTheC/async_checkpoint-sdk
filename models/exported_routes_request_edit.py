from pydantic import BaseModel, Field


class ExportedRoutesRequestEdit(BaseModel):
    internal_interfaces: bool = Field(
        alias="internal-interfaces",
        description="""<html>Specifies to export networks from interfaces with Topology 'Internal' from the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    static_routes: bool = Field(
        alias="static-routes",
        description="""<html>Specifies to export static routes from the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    custom_routes: bool = Field(
        alias="custom-routes",
        description="""<html>Specifies to export user-defined networks from the Security Gateway.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
    custom_routes_object: str = Field(
        alias="custom-routes-object",
        description="""<html>Specifies the name of the Network object or Network Group object that represents the exported routes.<br><b>Relevant only in Route-Based VPN Communities</b></html>.""",
    )
