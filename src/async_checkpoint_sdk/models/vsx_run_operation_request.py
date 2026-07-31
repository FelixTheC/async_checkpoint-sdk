from pydantic import BaseModel, Field
from vsx_add_member_request import VsxAddMemberRequest
from vsx_downgrade_request import VsxDowngradeRequest
from vsx_reconfigure_gw_request import VsxReconfigureGwRequest
from vsx_reconfigure_member_request import VsxReconfigureMemberRequest
from vsx_remove_member_request import VsxRemoveMemberRequest
from vsx_upgrade_request import VsxUpgradeRequest


class VsxRunOperationRequest(BaseModel):
    operation: str = Field(
        alias="operation",
        description="""The name of the operation to run. Each operation has its specific parameters.<br>The available operations are:<ul><li><i>upgrade</i> - Upgrades the VSX Gateway or VSX Cluster object to a higher version</li><li><i>downgrade</i> - Downgrades the VSX Gateway or VSX Cluster object to a lower version</li><li><i>add-member</i> - Adds a new VSX Cluster member object</li><li><i>remove-member</i> - Removes a VSX Cluster member object</li><li><i>reconf-gw</i> - Reconfigures a VSX Gateway after a clean install</li><li><i>reconf-member</i> - Reconfigures a VSX Cluster member after a clean install</li></ul>.""",
    )
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
