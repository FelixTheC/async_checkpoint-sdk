from add import Add
from log_exporter_attachments_request import LogExporterAttachmentsRequest
from log_exporter_data_manipulation_request import LogExporterDataManipulationRequest
from pydantic import BaseModel, Field
from remove import Remove


class LogExporterRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    target_server: str = Field(
        alias="target-server", description="""Target server port to which logs are exported."""
    )
    target_port: int = Field(
        alias="target-port", description="""Port number of the target server."""
    )
    protocol: str = Field(
        alias="protocol", description="""Protocol used to send logs to the target server."""
    )
    enabled: bool = Field(alias="enabled", description="""Indicates whether to enable export.""")
    attachments: LogExporterAttachmentsRequest = Field(
        alias="attachments", description="""Log exporter attachments."""
    )
    data_manipulation: LogExporterDataManipulationRequest = Field(
        alias="data-manipulation", description="""Log exporter data manipulation."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
