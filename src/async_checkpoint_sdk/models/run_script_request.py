from .pydantic import BaseModel, Field


class RunScriptRequest(BaseModel):
    script_type: str = Field(
        alias="script-type",
        description="""Type of script. Run a new script (one time) or an existing script from .the repository (repository).""",
    )
    script_base64: str = Field(
        alias="script-base64",
        description="""The entire content of the script encoded in Base64.<br><font color=red>Required only for</font> script-type one time.""",
    )
    args: str = Field(alias="args", description="""Script arguments.""")
    comments: str = Field(alias="comments", description="""Comments string.""")
    timeout: int = Field(
        alias="timeout",
        description="""Optional script timeout in seconds. Should be positive integer value.""",
    )
