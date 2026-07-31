from .pydantic import BaseModel, Field


class LogExporterAttachmentsReply(BaseModel):
    add_link_to_log_attachment: bool = Field(
        alias="add-link-to-log-attachment",
        description="""Indicates whether to add link to log attachment in SmartView.""",
    )
    add_link_to_log_details: bool = Field(
        alias="add-link-to-log-details",
        description="""Indicates whether to add link to log details in SmartView.""",
    )
    add_log_attachment_id: bool = Field(
        alias="add-log-attachment-id",
        description="""Indicates whether to add log attachment ID.""",
    )
