from pydantic import BaseModel, Field
from scep_settings_request import ScepSettingsRequest


class AutomaticEnrollmentRequest(BaseModel):
    automatically_enroll_certificate: bool = Field(
        alias="automatically-enroll-certificate",
        description="""Whether to automatically enroll certificate.""",
    )
    protocol: str = Field(
        alias="protocol",
        description="""Protocol that communicates with the certificate authority. Available only if automatically-enroll-certificate parameter is set to true.""",
    )
    scep_settings: ScepSettingsRequest = Field(
        alias="scep-settings",
        description="""Scep protocol settings. Available only if protocol is set to scep.""",
    )
