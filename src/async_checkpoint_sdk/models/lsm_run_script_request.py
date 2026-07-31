from pydantic import BaseModel, Field


class LsmRunScriptRequest(BaseModel):
    script_base64: str = Field(
        alias="script-base64", description="""The entire content of the script encoded in Base64."""
    )
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their name, or object unique identifier.""",
    )
