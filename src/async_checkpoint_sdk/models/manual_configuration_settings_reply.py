from pydantic import BaseModel, Field


class ManualConfigurationSettingsReply(BaseModel):
    internal_users: bool = Field(alias="internal-users", description="""Internal users.""")
    external_user_profiles: bool = Field(
        alias="external-user-profiles", description="""External user profiles."""
    )
    ldap_users: bool = Field(alias="ldap-users", description="""LDAP users.""")
    ldap_scope: str = Field(alias="ldap-scope", description="""LDAP directory scope.""")
    specific_directories: list[str] = Field(
        alias="specific-directories",
        description="""List of specific LDAP directory object references. Required when ldap-scope is set to 'specific'. User directories can be added by name or uid.""",
    )
