from config import Config
from aiohttp import ClientSession
from models.interoperable_device_request_new import InteroperableDeviceRequestNew
from models.interoperable_device_reply import InteroperableDeviceReply


async def add_interoperable_device(
    client: ClientSession, data: InteroperableDeviceRequestNew, config: Config, **kwargs
) -> InteroperableDeviceReply:
    """
    Add new Interoperable Device.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : InteroperableDeviceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InteroperableDeviceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-interoperable-device"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InteroperableDeviceReply(**resp)
