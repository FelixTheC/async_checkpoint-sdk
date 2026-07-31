from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_api_result_link_reply import WebApiResultLinkReply
from async_checkpoint_sdk.models.web_api_result_link_request import WebApiResultLinkRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def result_link(
    client: ClientSession, data: WebApiResultLinkRequest, config: SDKConfig, **kwargs
) -> WebApiResultLinkReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebApiResultLinkRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebApiResultLinkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/result-link"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebApiResultLinkReply(**resp)
