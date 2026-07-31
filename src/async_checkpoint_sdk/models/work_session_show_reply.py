from .administrator_reply import AdministratorReply
from .api_date_reply import ApiDateReply
from .api_domain_identifier import ApiDomainIdentifier
from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class WorkSessionShowReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    administrator: AdministratorReply = Field(
        alias="administrator",
        description="""The connected Administrator. Available only if detailed-admin-info is set to true.<br>The Administrator's permissions-profile/multi-domain-profile is presented only for the current connected session.""",
    )
    application: str = Field(
        alias="application",
        description="""The name of the application serving the Management API requests.""",
    )
    changes: int = Field(alias="changes", description="""Number of pending changes.""")
    connected_server: ApiObjectStandardIdentifier = Field(
        alias="connected-server",
        description="""The server which the user is currently connected to.""",
    )
    connection_mode: str = Field(
        alias="connection-mode", description="""Session connection mode."""
    )
    description: str = Field(alias="description", description="""Session description.""")
    email: str = Field(alias="email", description="""Administrator email.""")
    expired_session: bool = Field(
        alias="expired-session", description="""True if the session is expired."""
    )
    in_work: bool = Field(alias="in-work", description="""True if the session is in work state.""")
    ip_address: str = Field(
        alias="ip-address",
        description="""IP address from .which the session was initiated.""",
    )
    last_login_time: ApiDateReply = Field(
        alias="last-login-time", description="""Session description."""
    )
    last_logout_time: ApiDateReply = Field(
        alias="last-logout-time",
        description="""Timestamp when user last accessed the management server.""",
    )
    locks: int = Field(alias="locks", description="""Number of locked objects.""")
    phone_number: str = Field(alias="phone-number", description="""Administrator phone number.""")
    publish_time: ApiDateReply = Field(
        alias="publish-time",
        description="""Timestamp when user published changes on the management server.""",
    )
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Session expiration timeout in seconds.""",
    )
    state: str = Field(alias="state", description="""Session state.""")
    user_name: str = Field(alias="user-name", description="""The name of the logged in user.""")
    workflow_history: str = Field(
        alias="workflow-history",
        description="""Show details per each workflow action.""",
    )
    workflow_state: str = Field(alias="workflow-state", description="""Workflow session state.""")
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
