from pydantic import BaseModel, Field


class IpsUpdateRequest(BaseModel):
    package_path: str = Field(alias="package-path", description="""Offline update package path.""")
