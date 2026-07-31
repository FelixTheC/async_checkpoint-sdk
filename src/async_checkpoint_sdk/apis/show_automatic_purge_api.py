from aiohttp import ClientSession

from async_checkpoint_sdk.models.automatic_purge_reply import AutomaticPurgeReply
from async_checkpoint_sdk.models.automatic_purge_request_show import AutomaticPurgeRequestShow
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_automatic_purge(
    client: ClientSession, data: AutomaticPurgeRequestShow, config: SDKConfig, **kwargs
) -> AutomaticPurgeReply:
    """
    Show Automatic Purge.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AutomaticPurgeRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutomaticPurgeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-automatic-purge"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AutomaticPurgeReply(**resp)
