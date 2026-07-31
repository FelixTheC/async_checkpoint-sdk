from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class PasscodeProfileRequestEdit(BaseModel):
    allow_simple_passcode: bool = Field(
        alias="allow-simple-passcode",
        description="""The passcode length is 4 and only numeric values allowed.""",
    )
    min_passcode_length: int = Field(
        alias="min-passcode-length",
        description="""Minimum passcode length - relevant if allow-simple-passcode is disable.""",
    )
    require_alphanumeric_passcode: bool = Field(
        alias="require-alphanumeric-passcode",
        description="""Require alphanumeric characters in the passcode - relevant if allow-simple-passcode is disable.""",
    )
    min_passcode_complex_characters: int = Field(
        alias="min-passcode-complex-characters",
        description="""Minimum number of complex characters (if require-alphanumeric-passcode is enabled). The number of the complex characters cannot be greater than number of the passcode length.""",
    )
    force_passcode_expiration: bool = Field(
        alias="force-passcode-expiration",
        description="""Enable/disable expiration date to the passcode.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    passcode_expiration_period: int = Field(
        alias="passcode-expiration-period",
        description="""The period in days after which the passcode will expire.""",
    )
    enable_inactivity_time_lock: bool = Field(
        alias="enable-inactivity-time-lock",
        description="""Lock the device if app is inactive.""",
    )
    max_inactivity_time_lock: int = Field(
        alias="max-inactivity-time-lock",
        description="""Time without user input before passcode must be re-entered (in minutes).""",
    )
    enable_passcode_failed_attempts: bool = Field(
        alias="enable-passcode-failed-attempts",
        description="""Exit after few failures in passcode verification.""",
    )
    max_passcode_failed_attempts: int = Field(
        alias="max-passcode-failed-attempts",
        description="""Number of failed attempts allowed.""",
    )
    enable_passcode_history: bool = Field(
        alias="enable-passcode-history",
        description="""Check passcode history for reparations.""",
    )
    passcode_history: int = Field(
        alias="passcode-history",
        description="""Number of passcodes that will be kept in history.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from .the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
