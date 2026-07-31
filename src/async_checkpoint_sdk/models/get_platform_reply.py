from .pydantic import BaseModel, Field


class GetPlatformReply(BaseModel):
    hardware: str = Field(alias="hardware", description="""Gateway platform hardware type.""")
    os_name: str = Field(alias="os-name", description="""Gateway platform operating system.""")
    version: str = Field(alias="version", description="""Gateway platform version.""")
