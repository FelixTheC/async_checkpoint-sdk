from .pydantic import BaseModel, Field


class CustomModeRequest(BaseModel):
    social_networking_widgets: str = Field(
        alias="social-networking-widgets",
        description="""Social networking widgets mode.""",
    )
    url_filtering: str = Field(alias="url-filtering", description="""URL filtering mode.""")
