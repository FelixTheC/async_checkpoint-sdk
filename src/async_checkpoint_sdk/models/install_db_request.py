from pydantic import BaseModel, Field


class InstallDbRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets",
        description="""Check Point host(s) with one or more Management Software Blades enabled. The targets can be identified by their name or unique identifier.""",
    )
