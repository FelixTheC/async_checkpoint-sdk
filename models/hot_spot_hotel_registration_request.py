from add import add
from pydantic import BaseModel, Field
from remove import remove


class HotSpotHotelRegistrationRequest(BaseModel):
    enable_registration: bool = Field(
        alias="enable-registration",
        description="""Set Enable registration to true in order to configure settings. Set Enable registration to false in order to cancel registration (the configurations below won't be available). When the feature is enabled, you have several minutes to complete registration.""",
    )
    local_subnets_access_only: bool = Field(
        alias="local-subnets-access-only", description="""Local subnets access only."""
    )
    registration_timeout: int = Field(
        alias="registration-timeout",
        description="""Maximum time (in seconds) to complete registration.""",
    )
    track_log: bool = Field(alias="track-log", description="""Track log.""")
    max_ip_access_during_registration: int = Field(
        alias="max-ip-access-during-registration",
        description="""Maximum number of addresses to allow access to during registration.""",
    )
    ports: add | remove | str | list[str] = Field(
        alias="ports",
        description="""Ports to be opened during registration (up to 10 ports).""",
    )
