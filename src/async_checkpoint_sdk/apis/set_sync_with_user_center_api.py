from aiohttp import ClientSession

from async_checkpoint_sdk.models.sync_user_center_reply import SyncUserCenterReply
from async_checkpoint_sdk.models.sync_user_center_request_edit import SyncUserCenterRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_sync_with_user_center(
    client: ClientSession, data: SyncUserCenterRequestEdit, config: SDKConfig, **kwargs
) -> SyncUserCenterReply:
    """
    Adds information to the Check Point UserCenter account product list. <br><br>For example: Gateway name, version and active blades. For more details see: <span class="show-only-in-doc-ui"><a data-toggle="modal" href=https://support.checkpoint.com/results/sk/sk94064><u>sk94064</u></a></span>.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : SyncUserCenterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SyncUserCenterReply
    data : SyncUserCenterRequestEdit [Argument]
        data : SyncUserCenterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SyncUserCenterReply
    data : SyncUserCenterRequestEdit [Argument]
        data : SyncUserCenterRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SyncUserCenterReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-sync-with-user-center"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SyncUserCenterReply(**resp)
