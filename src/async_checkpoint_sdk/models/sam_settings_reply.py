from purge_sam_file_reply import PurgeSamFileReply
from pydantic import BaseModel, Field
from use_early_versions_reply import UseEarlyVersionsReply


class SamSettingsReply(BaseModel):
    forward_to_other_sam_servers: bool = Field(
        alias="forward-to-other-sam-servers",
        description="""Forward SAM clients' requests to other SAM servers.""",
    )
    use_early_versions: UseEarlyVersionsReply = Field(
        alias="use-early-versions", description="""N/A"""
    )
    purge_sam_file: PurgeSamFileReply = Field(
        alias="purge-sam-file", description="""Purge SAM File."""
    )
