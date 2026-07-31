from aiohttp import ClientSession

from async_checkpoint_sdk.models.disconnect_reply import DisconnectReply
from async_checkpoint_sdk.models.disconnect_request import DisconnectRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def disconnect(
    client: ClientSession, data: DisconnectRequest, config: SDKConfig, **kwargs
) -> DisconnectReply:
    """
    Disconnect a private session.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DisconnectRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DisconnectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/disconnect"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DisconnectReply(**resp)
