from pydantic import BaseModel, Field


class AccessControlPolicyLayersDomainPermissionsRequest(BaseModel):
    edit_layers: str = Field(
        alias="edit-layers",
        description="""By Software Blades - Edit Access Control layers that contain the blades enabled in the Permissions Profile.<br>By Selected Profile In A Layer Editor - Administrators can only edit the layer if the Access Control layer editor gives editing permission to their profiles.""",
    )
    app_control_and_url_filtering: bool = Field(
        alias="app-control-and-url-filtering",
        description="""Use Application and URL Filtering in Access Control rules.<br>Available only if edit-layers is set to By Software Blades.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness",
        description="""Use specified data types in Access Control rules.<br>Available only if edit-layers is set to By Software Blades.""",
    )
    firewall: bool = Field(
        alias="firewall",
        description="""Work with Access Control and other Software Blades that do not have their own Policies.<br>Available only if edit-layers is set to By Software Blades.""",
    )
    mobile_access: bool = Field(
        alias="mobile-access",
        description="""Work with Mobile Access rules.<br>Available only if edit-layers is set to By Software Blades.""",
    )
