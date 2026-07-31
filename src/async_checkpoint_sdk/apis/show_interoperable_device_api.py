from aiohttp import ClientSession

from async_checkpoint_sdk.models.interoperable_device_reply import InteroperableDeviceReply
from async_checkpoint_sdk.models.interoperable_device_request_show import (
    InteroperableDeviceRequestShow,
)
from config import Config


async def show_interoperable_device(
    client: ClientSession, data: InteroperableDeviceRequestShow, config: Config, **kwargs
) -> InteroperableDeviceReply:
    """
    Retrieves existing Interoperable Device.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : InteroperableDeviceRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InteroperableDeviceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-interoperable-device"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InteroperableDeviceReply(**resp)
