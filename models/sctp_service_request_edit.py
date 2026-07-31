from add import add
from aggressive_aging_request import AggressiveAgingRequest
from pydantic import BaseModel, Field
from remove import remove


class SctpServiceRequestEdit(BaseModel):
    aggressive_aging: AggressiveAgingRequest = Field(
        alias="aggressive-aging",
        description="""Sets short (aggressive) timeouts for idle connections.""",
    )
    keep_connections_open_after_policy_installation: bool = Field(
        alias="keep-connections-open-after-policy-installation",
        description="""Keep connections open after policy has been installed even if they are not allowed under the new policy. This overrides the settings in the Connection Persistence page. If you change this property, the change will not affect open connections, but only future connections.""",
    )
    match_for_any: bool = Field(
        alias="match-for-any",
        description="""Indicates whether this service is used when 'Any' is set as the rule's service and there are several service objects with the same source port and protocol.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    port: str = Field(
        alias="port",
        description="""Port number. To specify a port range add a hyphen between the lowest and the highest port numbers, for example 44-45.""",
    )
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Time (in seconds) before the session times out.""",
    )
    source_port: str = Field(
        alias="source-port",
        description="""Source port number. To specify a port range add a hyphen between the lowest and the highest port numbers, for example 44-45.""",
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
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
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
