from override_global_settings_request import OverrideGlobalSettingsRequest
from pydantic import BaseModel, Field


class AppiSettingsRequest(BaseModel):
    global_settings_mode: str = Field(
        alias="global-settings-mode",
        description="""Whether to override global settings or not.""",
    )
    override_global_settings: OverrideGlobalSettingsRequest = Field(
        alias="override-global-settings",
        description="""override global settings object.""",
    )
