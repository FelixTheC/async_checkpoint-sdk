from aiohttp import ClientSession

from async_checkpoint_sdk.models.indicator_reply import IndicatorReply
from async_checkpoint_sdk.models.indicator_request_edit import IndicatorRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_threat_indicator(
    client: ClientSession, data: IndicatorRequestEdit, config: SDKConfig, **kwargs
) -> IndicatorReply:
    """
    Edit an existing Threat-Indicator.

    Parameters
    ----------
    client : ClientSession
    data : IndicatorRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IndicatorReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-indicator"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IndicatorReply(**resp)
