from enrollment_settings_request import EnrollmentSettingsRequest
from pydantic import BaseModel, Field


class CertificateEnrollmentRequest(BaseModel):
    enrollment_settings: EnrollmentSettingsRequest = Field(
        alias="enrollment-settings", description="""Enrollment settings."""
    )
    enrollment_type: str = Field(
        alias="enrollment-type",
        description="""Weather to enroll certificate manually or automatically. Editable only if the Certificate Authority's automatic enrollment is enabled.""",
    )
