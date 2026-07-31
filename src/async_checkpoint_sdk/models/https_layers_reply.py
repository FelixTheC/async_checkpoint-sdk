from .api_object_standard_identifier import ApiObjectStandardIdentifier
from .pydantic import BaseModel, Field


class HttpsLayersReply(BaseModel):
    inbound_https_layer: ApiObjectStandardIdentifier = Field(
        alias="inbound-https-layer",
        description="""HTTPS inspection policy inbound layer. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    outbound_https_layer: ApiObjectStandardIdentifier = Field(
        alias="outbound-https-layer",
        description="""HTTPS inspection policy outbound layer. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
