from api_domain_identifier import ApiDomainIdentifier
from api_object_standard_identifier import ApiObjectStandardIdentifier
from available_actions_reply import AvailableActionsReply
from cvp_object_reply import CvpObjectReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class FtpResourceReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    exception_track: ApiObjectStandardIdentifier = Field(
        alias="exception-track",
        description="""The exception track to be used to log actions taken as a result of a match on the resource.""",
    )
    type: str = Field(alias="type", description="""Object type.""")
    resource_path: str = Field(
        alias="resource-path", description="""Refers to a location on the FTP server."""
    )
    resource_matching_method: str = Field(
        alias="resource-matching-method",
        description="""CVP server identified by name or UID.
The CVP server must already be defined as an OPSEC Application.""",
    )
    cvp: CvpObjectReply = Field(
        alias="cvp", description="""Configure CVP inspection on mail messages."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain", description="""Information about the domain that holds the Object."""
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions", description="""Actions that are available on the object."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
