from aiohttp import ClientSession

from async_checkpoint_sdk.models.cifs_resource_reply import CifsResourceReply
from async_checkpoint_sdk.models.cifs_resource_request_edit import CifsResourceRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_resource_cifs(
    client: ClientSession, data: CifsResourceRequestEdit, config: SDKConfig, **kwargs
) -> CifsResourceReply:
    """
    Clone existing object.

    Parameters
    ----------
    client : ClientSession
    data : CifsResourceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    CifsResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-cifs"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CifsResourceReply(**resp)
