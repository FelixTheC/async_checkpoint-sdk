from .pydantic import BaseModel, Field
from .uri_resource_wildcards_methods_request import UriResourceWildcardsMethodsRequest
from .uri_resource_wildcards_schemes_request import UriResourceWildcardsSchemesRequest


class UriResourceWildcardsRequest(BaseModel):
    schemes: UriResourceWildcardsSchemesRequest = Field(
        alias="schemes",
        description="""Select the URI Schemes to which this resource applies.""",
    )
    methods: UriResourceWildcardsMethodsRequest = Field(
        alias="methods",
        description="""Select the URI Schemes to which this resource applies.""",
    )
    host: str = Field(
        alias="host",
        description="""The functionality of the Host parameter depends on the DNS setup of the addressed server. For the host, only the IP address or the full DNS name should be used.""",
    )
    path: str = Field(
        alias="path",
        description="""Name matching is based on appending the file name in the request to the current working directory (unless the file name is already a full path name) and comparing the result to the path specified in the Resource definition.""",
    )
    query: str = Field(
        alias="query",
        description="""The parameters that are sent to the URI when it is accessed.""",
    )
