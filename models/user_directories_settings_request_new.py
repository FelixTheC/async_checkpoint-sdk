from manual_configuration_settings_request_new import (
    ManualConfigurationSettingsRequestNew,
)
from pydantic import BaseModel, Field


class UserDirectoriesSettingsRequestNew(BaseModel):
    configuration_mode: str = Field(
        alias="configuration-mode",
        description="""User directory configuration mode. When set to manual, manual-configuration section is required.""",
    )
    manual_configuration: ManualConfigurationSettingsRequestNew = Field(
        alias="manual-configuration",
        description="""Manual configuration settings for user directories. Required when configuration-mode is set to manual.""",
    )
    ldap_lookup_type: str = Field(
        alias="ldap-lookup-type",
        description="""LDAP user lookup attribute type. This setting applies to both modes automatic and manual configuration only when ldap-users is enabled.""",
    )
    custom_field: str = Field(
        alias="custom-field",
        description="""Custom LDAP field for lookup. Required when ldap-lookup-type is set to 'custom'.""",
    )
