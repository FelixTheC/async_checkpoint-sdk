from aiohttp import ClientSession

from async_checkpoint_sdk.models.tacacs_reply import TacacsReply
from async_checkpoint_sdk.models.tacacs_request_new import TacacsRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_tacacs_server(
    client: ClientSession, data: TacacsRequestNew, config: SDKConfig, **kwargs
) -> TacacsReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : TacacsRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TacacsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-tacacs-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TacacsReply(**resp)
