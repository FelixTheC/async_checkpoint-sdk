from pydantic import BaseModel, Field


class HttpsLayersRequestEdit(BaseModel):
    inbound_https_layer: str = Field(
        alias="inbound-https-layer",
        description="""HTTPS inspection policy inbound layer identified by name or UID.""",
    )
    outbound_https_layer: str = Field(
        alias="outbound-https-layer",
        description="""HTTPS inspection policy outbound layer identified by name or UID.""",
    )
