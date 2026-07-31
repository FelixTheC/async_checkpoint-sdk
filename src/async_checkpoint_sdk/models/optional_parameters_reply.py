from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class OptionalParametersReply(BaseModel):
    use_primary_dns_server: bool = Field(
        alias="use-primary-dns-server", description="""Use Primary DNS Server."""
    )
    primary_dns_server: ApiObjectStandardIdentifier = Field(
        alias="primary-dns-server",
        description="""Primary DNS Server. Identified by name or UID.
Must be set when use-primary-dns-server is true and can not be set when use-primary-dns-server is false.""",
    )
    use_first_backup_dns_server: bool = Field(
        alias="use-first-backup-dns-server", description="""Use First Backup DNS Server."""
    )
    first_backup_dns_server: ApiObjectStandardIdentifier = Field(
        alias="first-backup-dns-server",
        description="""First Backup DNS Server. Identified by name or UID.
Must be set when use-first-backup-dns-server is true and can not be set when use-first-backup-dns-server is false.""",
    )
    use_second_backup_dns_server: bool = Field(
        alias="use-second-backup-dns-server", description="""Use Second Backup DNS Server."""
    )
    second_backup_dns_server: ApiObjectStandardIdentifier = Field(
        alias="second-backup-dns-server",
        description="""Second Backup DNS Server. Identified by name or UID.
Must be set when use-second-backup-dns-server is true and can not be set when use-second-backup-dns-server is false.""",
    )
    dns_suffixes: str = Field(alias="dns-suffixes", description="""DNS Suffixes.""")
    use_primary_wins_server: bool = Field(
        alias="use-primary-wins-server", description="""Use Primary WINS Server."""
    )
    primary_wins_server: ApiObjectStandardIdentifier = Field(
        alias="primary-wins-server",
        description="""Primary WINS Server. Identified by name or UID.
Must be set when use-primary-wins-server is true and can not be set when use-primary-wins-server is false.""",
    )
    use_first_backup_wins_server: bool = Field(
        alias="use-first-backup-wins-server", description="""Use First Backup WINS Server."""
    )
    first_backup_wins_server: ApiObjectStandardIdentifier = Field(
        alias="first-backup-wins-server",
        description="""First Backup WINS Server. Identified by name or UID.
Must be set when use-first-backup-wins-server is true and can not be set when use-first-backup-wins-server is false.""",
    )
    use_second_backup_wins_server: bool = Field(
        alias="use-second-backup-wins-server", description="""Use Second Backup WINS Server."""
    )
    second_backup_wins_server: ApiObjectStandardIdentifier = Field(
        alias="second-backup-wins-server",
        description="""Second Backup WINS Server. Identified by name or UID.
Must be set when use-second-backup-wins-server is true and can not be set when use-second-backup-wins-server is false.""",
    )
    ip_lease_duration: int = Field(
        alias="ip-lease-duration",
        description="""IP Lease Duration in Minutes. The value must be in the range 2-32767.""",
    )
