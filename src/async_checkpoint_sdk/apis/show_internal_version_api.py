from aiohttp import ClientSession

from async_checkpoint_sdk.models.version_internal_reply import VersionInternalReply
from async_checkpoint_sdk.models.version_internal_request import VersionInternalRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_internal_version(
    client: ClientSession, data: VersionInternalRequest, config: SDKConfig, **kwargs
) -> VersionInternalReply:
    """
    Parameters
    ----------
    client : ClientSession
    data : VersionInternalRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    VersionInternalReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-internal-version"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VersionInternalReply(**resp)
