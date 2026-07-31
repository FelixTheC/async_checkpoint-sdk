from .add import add
from .pydantic import BaseModel, Field
from .remove import remove


class LimitRequestEdit(BaseModel):
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
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
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
