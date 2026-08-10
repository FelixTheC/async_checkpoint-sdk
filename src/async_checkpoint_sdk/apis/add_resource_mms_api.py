from aiohttp import ClientSession

from async_checkpoint_sdk.models.mms_resource_reply import MmsResourceReply
from async_checkpoint_sdk.models.mms_resource_request_new import MmsResourceRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_resource_mms(
    client: ClientSession, data: MmsResourceRequestNew, config: SDKConfig, **kwargs
) -> MmsResourceReply:
    """
    Create new MMS resource.

    Parameters
    ----------
    client : ClientSession
    data : MmsResourceRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MmsResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-mms"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MmsResourceReply(**resp)
