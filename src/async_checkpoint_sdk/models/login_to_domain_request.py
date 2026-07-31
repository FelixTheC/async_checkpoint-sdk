from pydantic import BaseModel, Field


class LoginToDomainRequest(BaseModel):
    domain: str = Field(alias="domain", description="""Domain identified by the name or UID.""")
    continue_last_session: bool = Field(
        alias="continue-last-session",
        description="""When 'continue-last-session' is set to 'True', the new session would continue where the last session was stopped. This option is available when the administrator has only one session that can be continued. If there is more than one session, see 'switch-session' API.""",
    )
    read_only: bool = Field(
        alias="read-only",
        description="""Login with Read Only permissions. This parameter is not considered in case continue-last-session is true.""",
    )
