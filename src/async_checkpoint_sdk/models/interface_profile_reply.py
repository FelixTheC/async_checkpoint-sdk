from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class InterfaceProfileReply(BaseModel):
    profile: ApiObjectStandardIdentifier = Field(
        alias="profile", description="""The Interface Profile object identified by Name or UID."""
    )
    custom_message_types: str = Field(
        alias="custom-message-types",
        description="""The messages types to match on them for this service. To specify a range, add a hyphen between the lowest and the highest numbers, for example: 32-35. Multiple Ranges can be chosen when separated with comma. This field relevant only when the Interface profile is set to 'Custom'.""",
    )
