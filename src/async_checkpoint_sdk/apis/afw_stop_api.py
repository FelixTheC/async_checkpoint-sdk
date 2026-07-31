from aiohttp import ClientSession

from async_checkpoint_sdk.models.afw_control_request import AfwControlRequest
from async_checkpoint_sdk.models.afw_control_service_reply import AfwControlServiceReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def afw_stop(
    client: ClientSession, data: AfwControlRequest, config: SDKConfig, **kwargs
) -> AfwControlServiceReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AfwControlRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AfwControlServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/afw-stop"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AfwControlServiceReply(**resp)
