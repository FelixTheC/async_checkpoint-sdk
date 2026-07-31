from .api_domain_identifier import ApiDomainIdentifier
from .available_actions_reply import AvailableActionsReply
from .meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from .pydantic import BaseModel, Field


class LimitReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    enable_download: bool = Field(
        alias="enable-download",
        description="""Enable throughput limit for downloads from .the internet to the organization.""",
    )
    download_rate: int = Field(
        alias="download-rate",
        description="""The Rate for the maximum permitted bandwidth.""",
    )
    download_unit: str = Field(
        alias="download-unit",
        description="""The Unit for the maximum permitted bandwidth.""",
    )
    enable_upload: bool = Field(
        alias="enable-upload",
        description="""Enable throughput limit for uploads from .the organization to the internet.""",
    )
    upload_rate: int = Field(
        alias="upload-rate",
        description="""The Rate for the maximum permitted bandwidth.""",
    )
    upload_unit: str = Field(
        alias="upload-unit",
        description="""The Unit for the maximum permitted bandwidth.""",
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
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
