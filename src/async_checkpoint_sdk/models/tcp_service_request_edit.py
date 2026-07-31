from .add import add
from .aggressive_aging_request import AggressiveAgingRequest
from .pydantic import BaseModel, Field
from .remove import remove


class TcpServiceRequestEdit(BaseModel):
    aggressive_aging: AggressiveAgingRequest = Field(
        alias="aggressive-aging",
        description="""Sets short (aggressive) timeouts for idle connections.""",
    )
    keep_connections_open_after_policy_installation: bool = Field(
        alias="keep-connections-open-after-policy-installation",
        description="""Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.""",
    )
    match_by_protocol_signature: bool = Field(
        alias="match-by-protocol-signature",
        description="""A value of true enables matching by the selected protocol's signature - the signature identifies the protocol as genuine. Select this option to limit the port to the specified protocol. If the selected protocol does not support matching by signature, this field cannot be set to true.""",
    )
    match_for_any: bool = Field(
        alias="match-for-any",
        description="""Indicates whether this service is used when 'Any' is set as the rule's service and there are several service objects with the same source port and protocol.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    override_default_settings: bool = Field(
        alias="override-default-settings",
        description="""Indicates whether this service is a Data Domain service which has been overridden.""",
    )
    port: str = Field(
        alias="port",
        description="""The number of the port used to provide this service. To specify a port range, place a hyphen between the lowest and highest port numbers, for example 44-55.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""Protocol name or uid. Select the protocol type associated with the service, and by implication, the management server (if any) that enforces Content Security and Authentication for the service. Selecting a Protocol Type invokes the specific protocol handlers for each protocol type, thus enabling higher level of security by parsing the protocol, and higher level of connectivity by tracking dynamic actions (such as opening of ports).<br>To remove, set value to 'none'.""",
    )
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Time (in seconds) before the session times out.""",
    )
    source_port: str = Field(
        alias="source-port",
        description="""Port number for the client side service. If specified, only those Source port Numbers will be Accepted, Dropped, or Rejected during packet inspection. Otherwise, the source port is not inspected.""",
    )
    use_default_session_timeout: bool = Field(
        alias="use-default-session-timeout",
        description="""Use default virtual session timeout.""",
    )
    enable_tcp_resource: bool = Field(
        alias="enable-tcp-resource", description="""Enable for tcp resource."""
    )
    sync_connections_on_cluster: bool = Field(
        alias="sync-connections-on-cluster",
        description="""Enables state-synchronized High Availability or Load Sharing on a ClusterXL or OPSEC-certified cluster.""",
    )
    use_delayed_sync: bool = Field(
        alias="use-delayed-sync",
        description="""Enable this option to delay notifying the Security Gateway about a connection, so that the connection will only be synchronized if it still exists x seconds after the connection is initiated. Relevant only for Clusters using an acceleration device supporting this feature.""",
    )
    delayed_sync_value: int = Field(
        alias="delayed-sync-value",
        description="""Specify the delay (in seconds) in which a synchronization will start after connection initiation.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    groups: add | remove | str | list[str] = Field(
        alias="groups", description="""Collection of group identifiers."""
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
