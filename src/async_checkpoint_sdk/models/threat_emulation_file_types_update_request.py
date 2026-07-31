from pydantic import BaseModel, Field


class ThreatEmulationFileTypesUpdateRequest(BaseModel):
    file_path: str = Field(
        alias="file-path",
        description="""File path for offline update of Threat Emulation file types, the file path should be on the management machine.""",
    )
