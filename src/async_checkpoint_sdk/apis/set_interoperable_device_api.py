from aiohttp import ClientSession

from async_checkpoint_sdk.models.interoperable_device_reply import InteroperableDeviceReply
from async_checkpoint_sdk.models.interoperable_device_request_edit import (
    InteroperableDeviceRequestEdit,
)
from config import Config


async def set_interoperable_device(
    client: ClientSession, data: InteroperableDeviceRequestEdit, config: Config, **kwargs
) -> InteroperableDeviceReply:
    """
    Edit existing Interoperable Device.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : InteroperableDeviceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InteroperableDeviceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-interoperable-device"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InteroperableDeviceReply(**resp)
