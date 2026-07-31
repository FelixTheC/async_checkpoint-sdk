from aiohttp import ClientSession

from config import Config
from models.api_query_object_reply import ApiQueryObjectReply
from models.trusted_ca_certificate_query_request import TrustedCaCertificateQueryRequest


async def show_cp_trusted_ca_certificates(
    client: ClientSession, data: TrustedCaCertificateQueryRequest, config: Config, **kwargs
) -> ApiQueryObjectReply:
    """
    Retrieve all objects.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedCaCertificateQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiQueryObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cp-trusted-ca-certificates"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiQueryObjectReply(**resp)
