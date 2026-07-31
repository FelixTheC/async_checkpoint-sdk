from pydantic import BaseModel, Field


class GatewaysDomainPermissionsRequest(BaseModel):
    smart_update: str = Field(
        alias="smart-update",
        description="""Install, update and delete Check Point licenses. This includes permissions to use SmartUpdate to manage licenses.""",
    )
    lsm_gw_db: str = Field(
        alias="lsm-gw-db",
        description="""Access to objects defined in LSM gateway tables. These objects are managed in the SmartProvisioning GUI or LSMcli command-line.<br>Note: 'Write' permission on lsm-gw-db allows administrator to run a script on SmartLSM gateway in Expert mode.""",
    )
    manage_provisioning_profiles: str = Field(
        alias="manage-provisioning-profiles",
        description="""Administrator can add, edit, delete, and assign provisioning profiles to gateways (both LSM and non-LSM).<br>Available for edit only if lsm-gw-db is set with 'Write' permission.<br>Note: 'Read' permission on lsm-gw-db enables 'Read' permission for manage-provisioning-profiles.""",
    )
    vsx_provisioning: bool = Field(
        alias="vsx-provisioning",
        description="""Create and configure Virtual Systems and other VSX virtual objects.""",
    )
    system_backup: bool = Field(alias="system-backup", description="""Backup Security Gateways.""")
    system_restore: bool = Field(
        alias="system-restore", description="""Restore Security Gateways from saved backups."""
    )
    open_shell: bool = Field(
        alias="open-shell", description="""Use the SmartConsole CLI to run commands."""
    )
    run_one_time_script: bool = Field(
        alias="run-one-time-script", description="""Run user scripts from the command line."""
    )
    run_repository_script: bool = Field(
        alias="run-repository-script", description="""Run scripts from the repository."""
    )
    manage_repository_scripts: str = Field(
        alias="manage-repository-scripts",
        description="""Add, change and remove scripts in the repository.""",
    )
