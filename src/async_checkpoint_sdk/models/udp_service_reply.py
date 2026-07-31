from .aggressive_aging_reply import AggressiveAgingReply
from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class UdpServiceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    accept_replies: bool = Field(alias="accept-replies", description="""N/A""")
    aggressive_aging: AggressiveAgingReply = Field(
        alias="aggressive-aging",
        description="""Sets short (aggressive) timeouts for idle connections.""",
    )
    groups: list[dict] = Field(
        alias="groups",
        description="""Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    keep_connections_open_after_policy_installation: bool = Field(
        alias="keep-connections-open-after-policy-installation",
        description="""Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.""",
    )
    match_by_protocol_signature: bool = Field(
        alias="match-by-protocol-signature",
        description="""A value of true enables matching by the selected protocol's signature - The signature identifies the protocol as genuine.""",
    )
    match_for_any: bool = Field(
        alias="match-for-any",
        description="""Indicates whether this service is used when 'Any' is set as the rule's service and there are several service objects with the same source port and protocol.""",
    )
    override_default_settings: bool = Field(
        alias="override-default-settings",
        description="""Indicates whether this service is a Data Domain service which has been overridden.""",
    )
    port: str = Field(
        alias="port",
        description="""The number of the port used to provide this service.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""The protocol type associated with the service, and by implication, the management server (if any) that enforces Content Security and Authentication for the service.""",
    )
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Time (in seconds) before the session times out.""",
    )
    source_port: str = Field(
        alias="source-port",
        description="""Port number for the client side service. If specified, only those Source port Numbers will be Accepted, Dropped, or Rejected during packet inspection. Otherwise, the source port is not inspected.""",
    )
    sync_connections_on_cluster: bool = Field(
        alias="sync-connections-on-cluster",
        description="""Enables state-synchronized High Availability or Load Sharing on a ClusterXL or OPSEC-certified cluster.""",
    )
    use_default_session_timeout: bool = Field(
        alias="use-default-session-timeout",
        description="""Use default virtual session timeout.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
