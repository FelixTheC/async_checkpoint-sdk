from host_ckp_log_settings_request_new import HostCkpLogSettingsRequestNew
from host_ckp_management_blades_request import HostCkpManagementBladesRequest
from host_interface_request_new import HostInterfaceRequestNew
from pydantic import BaseModel, Field
from third_party_nat_request import ThirdPartyNatRequest


class HostCkpRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    ip_address: str = Field(
        alias="ip-address",
        description="""IPv4 or IPv6 address. If both addresses are required use ipv4-address and ipv6-address fields explicitly.""",
    )
    interfaces: HostInterfaceRequestNew | list[dict] = Field(
        alias="interfaces", description="""Check Point host interfaces."""
    )
    nat_settings: ThirdPartyNatRequest = Field(
        alias="nat-settings", description="""NAT settings."""
    )
    one_time_password: str = Field(
        alias="one-time-password", description="""Secure internal connection one time password."""
    )
    hardware: str = Field(alias="hardware", description="""Hardware name.""")
    os: str = Field(alias="os", description="""Operating system name.""")
    version: str = Field(alias="version", description="""Check Point host platform version.""")
    management_blades: HostCkpManagementBladesRequest = Field(
        alias="management-blades", description="""Management blades."""
    )
    logs_settings: HostCkpLogSettingsRequestNew = Field(
        alias="logs-settings", description="""Logs settings."""
    )
    save_logs_locally: bool = Field(
        alias="save-logs-locally", description="""Enable save logs locally."""
    )
    send_alerts_to_server: str | list[str] = Field(
        alias="send-alerts-to-server",
        description="""Collection of Server(s) to send alerts to identified by the name or UID.""",
    )
    send_logs_to_backup_server: str | list[str] = Field(
        alias="send-logs-to-backup-server",
        description="""Collection of Backup server(s) to send logs to identified by the name or UID.""",
    )
    send_logs_to_server: str | list[str] = Field(
        alias="send-logs-to-server",
        description="""Collection of Server(s) to send logs to identified by the name or UID.""",
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
