from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from log_exporter_attachments_reply import LogExporterAttachmentsReply
from log_exporter_data_manipulation_reply import LogExporterDataManipulationReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class LogExporterReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    target_server: str = Field(
        alias="target-server",
        description="""Target server port to which logs are exported.""",
    )
    target_port: int = Field(
        alias="target-port", description="""Port number of the target server."""
    )
    protocol: str = Field(
        alias="protocol",
        description="""Protocol used to send logs to the target server.""",
    )
    enabled: bool = Field(
        alias="enabled", description="""Indicates whether to enable export."""
    )
    attachments: LogExporterAttachmentsReply = Field(
        alias="attachments", description="""Log exporter attachments."""
    )
    data_manipulation: LogExporterDataManipulationReply = Field(
        alias="data-manipulation", description="""Log exporter data manipulation."""
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
