from .pydantic import BaseModel, Field


class ThreatEmulationFileTypesUpdateReply(BaseModel):
    message: str = Field(alias="message", description="""Operation status.""")
