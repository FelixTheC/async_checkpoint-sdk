from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.indicator_request_new import IndicatorRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_threat_indicator(
    client: ClientSession, data: IndicatorRequestNew, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Create a new Threat-Indicator.

    Parameters
    ----------
    client : ClientSession
    data : IndicatorRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiTaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-threat-indicator"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
