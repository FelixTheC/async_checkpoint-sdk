from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class SecurityReply(BaseModel):
    session_timeout: int = Field(
        alias="session-timeout",
        description="""Session timeout - you can choose a unit (day, week, month) in session-timeout-unit field.""",
    )
    session_timeout_unit: str = Field(
        alias="session-timeout-unit",
        description="""Unit for session-timeout numeric value.""",
    )
    activate_passcode_lock: bool = Field(
        alias="activate-passcode-lock",
        description="""Require passcode to the application.""",
    )
    allow_store_credentials: bool = Field(
        alias="allow-store-credentials",
        description="""Allow storing the credentials on the device.""",
    )
    passcode_profile: ApiObjectStandardIdentifier = Field(
        alias="passcode-profile",
        description="""Passcode Policy object identified by the name or UID.""",
    )
    report_jailbroken: bool = Field(
        alias="report-jailbroken",
        description="""Issue log when device is detected as jail broken.""",
    )
    block_jailbroken: str = Field(
        alias="block-jailbroken",
        description="""Action upon detection of jail broken devices.""",
    )
    block_3rd_party_keyboard: bool = Field(
        alias="block-3rd-party-keyboard", description="""Block 3rd party keyboard."""
    )
    hide_ssl_connect_anyway_button: bool = Field(
        alias="hide-ssl-connect-anyway-button",
        description="""Hide connect button on critical SSL trust failures.""",
    )
