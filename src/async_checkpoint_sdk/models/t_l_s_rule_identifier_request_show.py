from hits_settings_request import HitsSettingsRequest
from pydantic import BaseModel, Field


class TLSRuleIdentifierRequestShow(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    layer: str = Field(
        alias="layer", description="""Layer that holds the Object. Identified by the Name or UID."""
    )
    show_hits: bool = Field(alias="show-hits", description="""Show hitcount data.""")
    hits_settings: HitsSettingsRequest = Field(
        alias="hits-settings",
        description="""Hitcount settings, define the range if hits to show.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
