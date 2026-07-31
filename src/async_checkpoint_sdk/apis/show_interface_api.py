from aiohttp import ClientSession

from async_checkpoint_sdk.models.interface_reply import InterfaceReply
from async_checkpoint_sdk.models.interface_request_show import InterfaceRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_interface(
    client: ClientSession, data: InterfaceRequestShow, config: SDKConfig, **kwargs
) -> InterfaceReply:
    """
    Retrieve existing network interface using object uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : InterfaceRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    InterfaceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-interface"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InterfaceReply(**resp)
