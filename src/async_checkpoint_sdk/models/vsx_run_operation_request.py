from .pydantic import BaseModel, Field
from .vsx_add_member_request import VsxAddMemberRequest
from .vsx_downgrade_request import VsxDowngradeRequest
from .vsx_reconfigure_gw_request import VsxReconfigureGwRequest
from .vsx_reconfigure_member_request import VsxReconfigureMemberRequest
from .vsx_remove_member_request import VsxRemoveMemberRequest
from .vsx_upgrade_request import VsxUpgradeRequest


class VsxRunOperationRequest(BaseModel):
    add_member_params: VsxAddMemberRequest = Field(
        alias="add-member-params",
        description="""Parameters for the operation to add a VSX Cluster member.""",
    )
    downgrade_params: VsxDowngradeRequest = Field(
        alias="downgrade-params",
        description="""Parameters for the operation to downgrade a VSX Gateway or VSX Cluster object to a lower version.<br>In case the current version is already the target version, or is lower than the target version, no change is done.""",
    )
    reconf_gw_params: VsxReconfigureGwRequest = Field(
        alias="reconf-gw-params",
        description="""Parameters for the operation to reconfigure a VSX Gateway after a clean install.""",
    )
    reconf_member_params: VsxReconfigureMemberRequest = Field(
        alias="reconf-member-params",
        description="""Parameters for the operation to reconfigure a VSX Cluster member after a clean install.""",
    )
    remove_member_params: VsxRemoveMemberRequest = Field(
        alias="remove-member-params",
        description="""Parameters for the operation to remove a VSX Cluster member object.""",
    )
    upgrade_params: VsxUpgradeRequest = Field(
        alias="upgrade-params",
        description="""Parameters for the operation to upgrade a VSX Gateway or VSX Cluster object to a higher version.<br>In case the current version is already the target version, or is higher than the target version, no change is done.""",
    )
