from aiohttp import ClientSession

from async_checkpoint_sdk.models.id_tag_reply import IdTagReply
from async_checkpoint_sdk.models.id_tag_request_edit import IdTagRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_identity_tag(
    client: ClientSession, data: IdTagRequestEdit, config: SDKConfig, **kwargs
) -> IdTagReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : IdTagRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    IdTagReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-identity-tag"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdTagReply(**resp)
