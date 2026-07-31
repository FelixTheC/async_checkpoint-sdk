from authentication_settings_edit import AuthenticationSettingsEdit
from identity_agent_portal_api_request import IdentityAgentPortalApiRequest
from pydantic import BaseModel, Field


class IdentityAgentSettingsEdit(BaseModel):
    agents_interval_keepalive: int = Field(
        alias="agents-interval-keepalive", description="""Agents send keepalive period (minutes)."""
    )
    user_reauthenticate_interval: int = Field(
        alias="user-reauthenticate-interval",
        description="""Agent reauthenticate time interval (minutes).""",
    )
    authentication_settings: AuthenticationSettingsEdit = Field(
        alias="authentication-settings",
        description="""Authentication Settings for Identity Agent.""",
    )
    identity_agent_portal_settings: IdentityAgentPortalApiRequest = Field(
        alias="identity-agent-portal-settings",
        description="""Identity Agent accessibility settings.""",
    )
