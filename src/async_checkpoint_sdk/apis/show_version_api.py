from aiohttp import ClientSession

from async_checkpoint_sdk.models.version_reply import VersionReply
from async_checkpoint_sdk.models.version_request import VersionRequest
from config import Config


async def show_version(
    client: ClientSession, data: VersionRequest, config: Config, **kwargs
) -> VersionReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : VersionRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    VersionReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-version"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return VersionReply(**resp)
