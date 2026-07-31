from pydantic import BaseModel, Field


class MaliciousLinksRequest(BaseModel):
    max_bytes: int = Field(
        alias="max-bytes",
        description="""Scan links in the first bytes of the mail body.""",
    )
    max_links: int = Field(
        alias="max-links", description="""Maximum links to scan in mail body."""
    )
