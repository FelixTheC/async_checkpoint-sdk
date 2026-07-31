from override_activation_by_profile_request import OverrideActivationByProfileRequest
from pydantic import BaseModel, Field
from remove import Remove


class ProtectionRequestEdit(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    comments: str = Field(alias="comments", description="""Protection comments.""")
    follow_up: bool = Field(
        alias="follow-up", description="""Tag the protection with pre-defined follow-up flag."""
    )
    overrides: Remove | OverrideActivationByProfileRequest | list[dict] = Field(
        alias="overrides",
        description="""Overrides per profile for this protection<br> Note: Removing an override for Core protections only removes the override for the selected action. Adding an override only affects that specific parameter.<br> Removing an override for Threat Cloud protections clears the action, tracking, and packet capture settings. Adding an override sets all three fields to their default values or the specified ones.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
