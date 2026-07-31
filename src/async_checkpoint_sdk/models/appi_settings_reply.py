from .override_global_settings_reply import OverrideGlobalSettingsReply
from .pydantic import BaseModel, Field


class AppiSettingsReply(BaseModel):
    global_settings_mode: str = Field(
        alias="global-settings-mode",
        description="""Whether to override global settings or not.""",
    )
    override_global_settings: OverrideGlobalSettingsReply = Field(
        alias="override-global-settings",
        description="""override global settings object.""",
    )
