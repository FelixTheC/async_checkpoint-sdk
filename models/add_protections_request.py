from pydantic import BaseModel, Field


class AddProtectionsRequest(BaseModel):
    package_format: str = Field(
        alias="package-format", description="""Protections package format."""
    )
    package_path: str = Field(
        alias="package-path", description="""Protections package path."""
    )
