from pydantic import BaseModel, Field


class WebApiLoginRequest(BaseModel):
    user: str = Field(alias="user", description="""Administrator user name.""")
    password: str = Field(alias="password", description="""Administrator password.""")
    continue_last_session: bool = Field(
        alias="continue-last-session",
        description="""When 'continue-last-session' is set to 'True', the new session would continue where the last session was stopped. This option is available when the administrator has only one session that can be continued. If there is more than one session, see 'switch-session' API.""",
    )
    domain: str = Field(
        alias="domain",
        description="""Use domain to login to specific domain. Domain can be identified by name or UID.""",
    )
    enter_last_published_session: bool = Field(
        alias="enter-last-published-session",
        description="""Login to the last published session. Such login is done with the Read Only permissions.""",
    )
    new_password: str = Field(
        alias="new-password",
        description="""Administrator new password. Can only be used for first login, when the administrator password must be changed.""",
    )
    read_only: bool = Field(
        alias="read-only",
        description="""Login with Read Only permissions. This parameter is not considered in case continue-last-session is true.""",
    )
    session_comments: str = Field(
        alias="session-comments",
        description="""Session comments. Can be viewed only using the show-session API.""",
    )
    session_description: str = Field(
        alias="session-description", description="""A description of the session's purpose."""
    )
    session_name: str = Field(alias="session-name", description="""Session unique name.""")
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Session expiration timeout in seconds. Default 600 seconds.""",
    )
