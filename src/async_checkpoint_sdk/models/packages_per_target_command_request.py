from packagesfilter import Packagesfilter
from pydantic import BaseModel, Field


class PackagesPerTargetCommandRequest(BaseModel):
    display: Packagesfilter = Field(
        alias="display", description="""Filter the displayed results."""
    )
    targets: str | list[str] = Field(
        alias="targets",
        description="""On what targets to execute this command. Targets may be identified by their object name, or object unique identifier.""",
    )
