from add import Add
from cvp_object_request import CvpObjectRequest
from pydantic import BaseModel, Field
from remove import Remove


class FtpResourceRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    exception_track: str = Field(
        alias="exception-track",
        description="""The UID or Name of the exception track to be used to log actions taken as a result of a match on the resource.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    resources_path: str = Field(
        alias="resources-path", description="""Refers to a location on the FTP server."""
    )
    resource_matching_method: str = Field(
        alias="resource-matching-method",
        description="""GET allows Downloads from the server to the client. PUT allows Uploads from the client to the server.""",
    )
    cvp: CvpObjectRequest = Field(
        alias="cvp", description="""Configure CVP inspection on mail messages."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: Add | Remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
