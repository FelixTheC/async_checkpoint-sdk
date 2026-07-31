from pydantic import BaseModel, Field


class Packagesfilter(BaseModel):
    category: str | list[str] = Field(
        alias="category", description="""The package categories to include in the results."""
    )
    installed: str = Field(
        alias="installed", description="""Show installed packages, available packages, or both."""
    )
    recommended: str = Field(
        alias="recommended",
        description="""Show only recommended packages, other packages, or both.""",
    )
