from object import Object
from pydantic import BaseModel, Field


class ServerCertificateRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    base64_certificate: str = Field(
        alias="base64-certificate",
        description="""Certificate file encoded in base64.<br/>Valid file formats: p12.<br/>If you changed the 'base64-certificate' parameter, you must also change the 'password' parameter.""",
    )
    base64_password: str = Field(
        alias="base64-password", description="""Base64 encoded password of the certificate file."""
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: Object = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
