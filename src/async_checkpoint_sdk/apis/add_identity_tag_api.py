from aiohttp import ClientSession

from async_checkpoint_sdk.models.id_tag_reply import IdTagReply
from async_checkpoint_sdk.models.id_tag_request_new import IdTagRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_identity_tag(
    client: ClientSession, data: IdTagRequestNew, config: SDKConfig, **kwargs
) -> IdTagReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : IdTagRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IdTagReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-identity-tag"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IdTagReply(**resp)
