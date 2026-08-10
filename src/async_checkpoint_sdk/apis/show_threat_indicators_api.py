from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_query_request import ApiQueryRequest
from async_checkpoint_sdk.models.indicator_query_reply import IndicatorQueryReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_threat_indicators(
    client: ClientSession, data: ApiQueryRequest, config: SDKConfig, **kwargs
) -> IndicatorQueryReply:
    """
    Display a list of Threat-Indicators.

    Parameters
    ----------
    client : ClientSession
    data : ApiQueryRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IndicatorQueryReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-indicators"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IndicatorQueryReply(**resp)
