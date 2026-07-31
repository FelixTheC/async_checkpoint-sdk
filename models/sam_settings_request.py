from purge_sam_file_request import PurgeSamFileRequest
from pydantic import BaseModel, Field
from use_early_versions_request import UseEarlyVersionsRequest


class SamSettingsRequest(BaseModel):
    forward_to_other_sam_servers: bool = Field(
        alias="forward-to-other-sam-servers",
        description="""Forward SAM clients' requests to other SAM servers.""",
    )
    use_early_versions: UseEarlyVersionsRequest = Field(
        alias="use-early-versions",
        description="""Use early versions compatibility mode.""",
    )
    purge_sam_file: PurgeSamFileRequest = Field(
        alias="purge-sam-file", description="""Purge SAM File."""
    )
