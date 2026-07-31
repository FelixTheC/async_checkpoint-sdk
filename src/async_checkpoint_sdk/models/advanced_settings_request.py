from pydantic import BaseModel, Field
from sam_settings_request import SamSettingsRequest


class AdvancedSettingsRequest(BaseModel):
    connection_persistence: str = Field(
        alias="connection-persistence",
        description="""Handling established connections when installing a new policy.""",
    )
    sam: SamSettingsRequest = Field(alias="sam", description="""SAM.""")
