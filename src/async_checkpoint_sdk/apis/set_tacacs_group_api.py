from aiohttp import ClientSession

from async_checkpoint_sdk.models.tacacs_group_reply import TacacsGroupReply
from async_checkpoint_sdk.models.tacacs_group_request_edit import TacacsGroupRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_tacacs_group(
    client: ClientSession, data: TacacsGroupRequestEdit, config: SDKConfig, **kwargs
) -> TacacsGroupReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : TacacsGroupRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TacacsGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-tacacs-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TacacsGroupReply(**resp)
