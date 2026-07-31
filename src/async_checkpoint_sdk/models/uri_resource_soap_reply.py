from pydantic import BaseModel, Field


class UriResourceSoapReply(BaseModel):
    inspection: str = Field(
        alias="inspection",
        description="""Allow all SOAP Requests, or Allow only SOAP requests specified in the following file-id.""",
    )
    file_id: str = Field(alias="file-id", description="""A file containing SOAP requests.""")
    track_connections: str = Field(
        alias="track-connections", description="""The method of tracking SOAP connections."""
    )
