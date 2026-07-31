from .pydantic import BaseModel, Field


class UpgradeExportRequest(BaseModel):
    version: str = Field(alias="version", description="""Target version.""")
    verify_all_servers: bool = Field(
        alias="verify-all-servers",
        description="""Runs the verification process on all Management Servers and Log Servers.<br>For more information see <span class=show-only-in-doc-ui><a data-toggle=modal href=https://support.checkpoint.com/results/sk/sk182144><u style=font-weight: bold;>sk182144</u></a></span>.""",
    )
    days_of_logs: int = Field(alias="days-of-logs", description="""Export <N> last days of logs.""")
    include_logs: bool = Field(
        alias="include-logs", description="""Export logs without log indexes."""
    )
    include_logs_indexes: bool = Field(
        alias="include-logs-indexes", description="""Export logs with log indexes."""
    )
    include_endpoint_configuration: bool = Field(
        alias="include-endpoint-configuration",
        description="""Include export of the Endpoint Security Management configuration files.""",
    )
    include_endpoint_database: bool = Field(
        alias="include-endpoint-database",
        description="""Include export of the Endpoint Security Management database.""",
    )
    is_domain_backup: bool = Field(
        alias="is-domain-backup",
        description="""If true, the exported Domain will be suitable for import on the same Multi-Domain Server only.""",
    )
    is_smc_to_mds: bool = Field(
        alias="is-smc-to-mds",
        description="""If true, the exported Security Management Server will be suitable for import on the Multi-Domain Server only.""",
    )
    pre_export_verification_only: bool = Field(
        alias="pre-export-verification-only",
        description="""If true, only runs the pre-export verifications instead of the full export.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings",
        description="""Ignoring the verification warnings. By Setting this parameter to 'true' export will not be blocked by warnings.""",
    )
