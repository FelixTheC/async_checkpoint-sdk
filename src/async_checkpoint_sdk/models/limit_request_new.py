from pydantic import BaseModel, Field


class LimitRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    enable_download: bool = Field(
        alias="enable-download",
        description="""Enable throughput limit for downloads from the internet to the organization.""",
    )
    download_rate: int = Field(
        alias="download-rate", description="""The Rate for the maximum permitted bandwidth."""
    )
    download_unit: str = Field(
        alias="download-unit", description="""The Unit for the maximum permitted bandwidth."""
    )
    enable_upload: bool = Field(
        alias="enable-upload",
        description="""Enable throughput limit for uploads from the organization to the internet.""",
    )
    upload_rate: int = Field(
        alias="upload-rate", description="""The Rate for the maximum permitted bandwidth."""
    )
    upload_unit: str = Field(
        alias="upload-unit", description="""The Unit for the maximum permitted bandwidth."""
    )
    set_if_exists: bool = Field(
        alias="set-if-exists",
        description="""If another object with the same identifier already exists, it will be updated. The command behaviour will be the same as if originally a set command was called. Pay attention that original object's fields will be overwritten by the fields provided in the request payload!""",
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
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
