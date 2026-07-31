from aggressive_aging_request import AggressiveAgingRequest
from pydantic import BaseModel, Field


class OtherServiceRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    accept_replies: bool = Field(
        alias="accept-replies",
        description="""Specifies whether Other Service replies are to be accepted.""",
    )
    action: str = Field(
        alias="action",
        description="""Contains an INSPECT expression that defines the action to take if a rule containing this service is matched.
Example: set r_mhandler &open_ssl_handler sets a handler on the connection.""",
    )
    aggressive_aging: AggressiveAgingRequest = Field(
        alias="aggressive-aging",
        description="""Sets short (aggressive) timeouts for idle connections.""",
    )
    ip_protocol: int = Field(alias="ip-protocol", description="""IP protocol number.""")
    keep_connections_open_after_policy_installation: bool = Field(
        alias="keep-connections-open-after-policy-installation",
        description="""Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.""",
    )
    match: str = Field(
        alias="match",
        description="""Contains an INSPECT expression that defines the matching criteria. The connection is examined against the expression during the first packet.
Example: tcp, dport = 21, direction = 0 matches incoming FTP control connections.""",
    )
    match_for_any: bool = Field(
        alias="match-for-any",
        description="""Indicates whether this service is used when 'Any' is set as the rule's service and there are several service objects with the same source port and protocol.""",
    )
    override_default_settings: bool = Field(
        alias="override-default-settings",
        description="""Indicates whether this service is a Data Domain service which has been overridden.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""Protocol name or uid. The protocol type associated with the service, and by implication,
the management server (if any) that enforces Content Security and Authentication for the service.""",
    )
    session_timeout: int = Field(
        alias="session-timeout", description="""Time (in seconds) before the session times out."""
    )
    sync_connections_on_cluster: bool = Field(
        alias="sync-connections-on-cluster",
        description="""Enables state-synchronized High Availability or Load Sharing on a ClusterXL or OPSEC-certified cluster.""",
    )
    use_default_session_timeout: bool = Field(
        alias="use-default-session-timeout", description="""Use default virtual session timeout."""
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
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
