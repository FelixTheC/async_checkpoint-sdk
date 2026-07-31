from pydantic import BaseModel, Field


class TrustedCaUpdateRequest(BaseModel):
    package_path: str = Field(
        alias="package-path",
        description="""Path on the management server for offline Trusted CAs package update.""",
    )
