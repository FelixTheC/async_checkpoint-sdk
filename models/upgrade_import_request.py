from pydantic import BaseModel, Field


class UpgradeImportRequest(BaseModel):
    domain_ipv6_address: str = Field(
        alias="domain-ipv6-address",
        description="""IPv6 address for the imported Domain.""",
    )
    days_of_logs: int = Field(
        alias="days-of-logs", description="""Export <N> last days of logs."""
    )
    include_logs: bool = Field(
        alias="include-logs", description="""Import logs without log indexes."""
    )
    include_logs_indexes: bool = Field(
        alias="include-logs-indexes", description="""Import logs with log indexes."""
    )
    keep_cloud_sharing: bool = Field(
        alias="keep-cloud-sharing",
        description="""Preserve the connection of the Management Server to Check Point's Infinity Portal.<br>Use this flag after ensuring that the original Management Server does not communicate with Infinity Portal.<br>Note: resuming the connection is also possible after import with set-cloud-services.""",
    )
    include_endpoint_configuration: bool = Field(
        alias="include-endpoint-configuration",
        description="""Include import of the Endpoint Security Management configuration files.""",
    )
    include_endpoint_database: bool = Field(
        alias="include-endpoint-database",
        description="""Include import of the Endpoint Security Management database.""",
    )
    verify_domain_restore: bool = Field(
        alias="verify-domain-restore",
        description="""If true, verify that the restore operation is valid for this input file and this environment. <br>Note: Restore operation will not be executed.""",
    )
    pre_import_verification_only: bool = Field(
        alias="pre-import-verification-only",
        description="""If true, only runs the pre-import verifications instead of the full import.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Ignoring the verification warnings. By Setting this parameter to 'true' import will not be blocked by warnings.""",
    )
