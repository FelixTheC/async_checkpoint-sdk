from .authentication_settings_reply import AuthenticationSettingsReply
from .i_d_a_portal_reply import IDAPortalReply
from .pydantic import BaseModel, Field


class IdentityAgentSettingsReply(BaseModel):
    agents_interval_keepalive: int = Field(
        alias="agents-interval-keepalive",
        description="""Agents send keepalive period (minutes).""",
    )
    authentication_settings: AuthenticationSettingsReply = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Agent.""",
    )
    identity_agent_portal_settings: IDAPortalReply = Field(
        alias="identity-agent-portal-settings",
        description="""Identity Agent accessibility settings.""",
    )
    user_reauthenticate_interval: int = Field(
        alias="user-reauthenticate-interval",
        description="""Agent reauthenticate time interval (minutes).""",
    )
