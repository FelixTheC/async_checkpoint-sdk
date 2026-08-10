from aiohttp import ClientSession

from async_checkpoint_sdk.models.appi_status_reply import AppiStatusReply
from async_checkpoint_sdk.models.appi_status_request import AppiStatusRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_app_control_status(
    client: ClientSession, data: AppiStatusRequest, config: SDKConfig, **kwargs
) -> AppiStatusReply:
    """
    Retrieve existing Application Control and URL Filtering update status.

    Parameters
    ----------
    client : ClientSession
    data : AppiStatusRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AppiStatusReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-app-control-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AppiStatusReply(**resp)
