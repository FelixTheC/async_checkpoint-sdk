from pydantic import BaseModel, Field


class CpPasswordRequirementsRequestEdit(BaseModel):
    min_password_length: int = Field(
        alias="min-password-length", description="""Minimum Check Point password length."""
    )
