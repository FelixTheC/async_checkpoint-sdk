from aiohttp import ClientSession

from async_checkpoint_sdk.models.base_domain_query_reply import BaseDomainQueryReply
from async_checkpoint_sdk.models.base_domain_query_request import BaseDomainQueryRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_domains(
    client: ClientSession, data: BaseDomainQueryRequest, config: SDKConfig, **kwargs
) -> BaseDomainQueryReply:
    """
    Retrieve all objects.

    Parameters
    ----------
    client : ClientSession
    data : BaseDomainQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    BaseDomainQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-domains"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return BaseDomainQueryReply(**resp)
