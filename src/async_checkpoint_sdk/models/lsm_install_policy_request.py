from pydantic import BaseModel, Field


class LsmInstallPolicyRequest(BaseModel):
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
