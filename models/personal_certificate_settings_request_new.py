from pydantic import BaseModel, Field


class PersonalCertificateSettingsRequestNew(BaseModel):
    fetch_username_from: str = Field(
        alias="fetch-username-from", description="""Fetch username from."""
    )
    storage_type: str = Field(
        alias="storage-type", description="""Certificate storage type."""
    )
    source: str = Field(
        alias="source",
        description="""Certificate source field, relevant only when using custom-fields for fetch-username-from.""",
    )
    dn_part: str = Field(
        alias="dn-part",
        description="""DN part to extract, relevant only when using custom-fields for fetch-username-from.""",
    )
    dn_concurrence: int = Field(
        alias="dn-concurrence",
        description="""DN part occurrence number, relevant only when using custom-fields for fetch-username-from.""",
    )
