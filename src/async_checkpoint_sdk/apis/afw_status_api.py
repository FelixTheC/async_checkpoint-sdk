from aiohttp import ClientSession

from async_checkpoint_sdk.models.afw_control_request import AfwControlRequest
from async_checkpoint_sdk.models.afw_control_status_reply import AfwControlStatusReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def afw_status(
    client: ClientSession, data: AfwControlRequest, config: SDKConfig, **kwargs
) -> AfwControlStatusReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : AfwControlRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AfwControlStatusReply

    """
    url = f"https://{config.server}:{config.port}/web_api/afw-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AfwControlStatusReply(**resp)
