from aiohttp import ClientSession

from async_checkpoint_sdk.models.sync_user_center_reply import SyncUserCenterReply
from async_checkpoint_sdk.models.sync_user_center_request_show import SyncUserCenterRequestShow
from config import Config


async def show_sync_with_user_center(
    client: ClientSession, data: SyncUserCenterRequestShow, config: Config, **kwargs
) -> SyncUserCenterReply:
    """
    This indicates whether the information is being synchronized with the user center.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SyncUserCenterRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SyncUserCenterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-sync-with-user-center"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SyncUserCenterReply(**resp)
