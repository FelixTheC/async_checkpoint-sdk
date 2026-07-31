from .pydantic import BaseModel, Field


class TrackSettingsForRequest(BaseModel):
    accounting: bool = Field(
        alias="accounting", description="""Turns accounting for track on and off."""
    )
    alert: str = Field(alias="alert", description="""Type of alert for the track.""")
    enable_firewall_session: bool = Field(
        alias="enable-firewall-session",
        description="""Determine whether to generate session log to firewall only connections.""",
    )
    per_connection: bool = Field(
        alias="per-connection",
        description="""Determines whether to perform the log per connection.""",
    )
    per_session: bool = Field(
        alias="per-session",
        description="""Determines whether to perform the log per session.""",
    )
    type: str = Field(alias="type", description="""Log, Extended Log, Detailed  Log, None.""")
