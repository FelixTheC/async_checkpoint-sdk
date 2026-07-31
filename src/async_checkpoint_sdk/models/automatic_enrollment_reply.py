from .cmpv1_settings_reply import Cmpv1SettingsReply
from .cmpv2_settings_reply import Cmpv2SettingsReply
from .pydantic import BaseModel, Field
from .scep_settings_reply import ScepSettingsReply


class AutomaticEnrollmentReply(BaseModel):
    automatically_enroll_certificate: bool = Field(
        alias="automatically-enroll-certificate",
        description="""Whether to automatically enroll certificate.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""Protocol that communicates with the certificate authority. Available only if automatically-enroll-certificate parameter is set to true.""",
    )
    scep_settings: ScepSettingsReply = Field(
        alias="scep-settings",
        description="""Scep protocol settings. Available only if protocol is set to scep.""",
    )
    cmpv1_settings: Cmpv1SettingsReply = Field(
        alias="cmpv1-settings",
        description="""Cmpv1 protocol settings. Available only if protocol is set to cmpv1.""",
    )
    cmpv2_settings: Cmpv2SettingsReply = Field(
        alias="cmpv2-settings",
        description="""Cmpv2 protocol settings. Available only if protocol is set to cmpv2.""",
    )
