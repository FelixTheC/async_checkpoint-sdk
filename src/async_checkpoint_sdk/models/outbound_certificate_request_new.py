from .pydantic import BaseModel, Field


class OutboundCertificateRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    public_key_algorithm: str = Field(
        alias="public-key-algorithm",
        description="""Public key algorithm and size of the outbound certificate.""",
    )
    is_default: bool = Field(
        alias="is-default",
        description="""Is the certificate the default certificate.""",
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
        alias="ignore-warnings",
        description="""Apply changes ignoring warnings. By Setting this parameter to 'true' default outbound certificate can be replaced.""",
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
