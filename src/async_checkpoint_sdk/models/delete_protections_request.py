from .pydantic import BaseModel, Field


class DeleteProtectionsRequest(BaseModel):
    package_format: str = Field(
        alias="package-format", description="""Protections package format."""
    )
