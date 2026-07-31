from api_object_standard_identifier import ApiObjectStandardIdentifier
from pydantic import BaseModel, Field


class IcmpOptionsReply(BaseModel):
    destination: ApiObjectStandardIdentifier | str = Field(
        alias="destination",
        description="""The probe destination. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    source: ApiObjectStandardIdentifier | str = Field(
        alias="source",
        description="""The probe source. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
