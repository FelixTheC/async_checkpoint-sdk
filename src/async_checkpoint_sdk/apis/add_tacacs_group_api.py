from aiohttp import ClientSession

from async_checkpoint_sdk.models.tacacs_group_reply import TacacsGroupReply
from async_checkpoint_sdk.models.tacacs_group_request_new import TacacsGroupRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_tacacs_group(
    client: ClientSession, data: TacacsGroupRequestNew, config: SDKConfig, **kwargs
) -> TacacsGroupReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : TacacsGroupRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TacacsGroupReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-tacacs-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TacacsGroupReply(**resp)
