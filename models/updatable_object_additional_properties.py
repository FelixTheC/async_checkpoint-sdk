from pydantic import BaseModel, Field


class UpdatableObjectAdditionalProperties(BaseModel):
    description: str = Field(
        alias="description",
        description="""Description of retrieved Updatable Object.""",
    )
    info_text: str = Field(
        alias="info-text",
        description="""Information about the Updatable Object IP ranges source.""",
    )
    info_url: str = Field(
        alias="info-url",
        description="""URL of the Updatable Object IP ranges source.""",
    )
    uri: str = Field(
        alias="uri",
        description="""URI of the Updatable Object under the Updatable Objects Repository.""",
    )
