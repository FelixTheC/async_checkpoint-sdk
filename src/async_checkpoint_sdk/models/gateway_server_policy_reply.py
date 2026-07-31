from .api_date_reply import ApiDateReply
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class GatewayServerPolicyReply(BaseModel):
    access_policy_installation_date: ApiDateReply = Field(
        alias="access-policy-installation-date",
        description="""Access policy installation date.""",
    )
    access_policy_installed: bool = Field(
        alias="access-policy-installed",
        description="""Gets true if access-policy was installed.""",
    )
    access_policy_name: str = Field(
        alias="access-policy-name", description="""Name of the access-policy."""
    )
    access_policy_revision: ApiObjectStandardIdentifier = Field(
        alias="access-policy-revision",
        description="""Revision of the installed access policy.""",
    )
    cluster_members_access_policy_revision: list[dict] = Field(
        alias="cluster-members-access-policy-revision",
        description="""Revisions of the access policy installed on each cluster member.""",
    )
    cluster_members_threat_policy_revision: list[dict] = Field(
        alias="cluster-members-threat-policy-revision",
        description="""Revisions of the threat policy installed on each cluster member.""",
    )
    threat_policy_installation_date: ApiDateReply = Field(
        alias="threat-policy-installation-date",
        description="""Threat policy installation date.""",
    )
    threat_policy_installed: bool = Field(
        alias="threat-policy-installed",
        description="""Gets true if threat-policy was installed.""",
    )
    threat_policy_name: str = Field(
        alias="threat-policy-name", description="""Name of the threat-policy."""
    )
    threat_policy_revision: ApiObjectStandardIdentifier = Field(
        alias="threat-policy-revision",
        description="""Revision of the installed threat policy.""",
    )
