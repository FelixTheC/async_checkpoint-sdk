from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.full_sync_request import FullSyncRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def ha_full_sync(
    client: ClientSession, data: FullSyncRequest, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Perform full sync from active server to standby peer. <br>Run this command from the active server. <br>When performing a full sync on the global domain, use the Multi Domain Server name of the standby global domain.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : FullSyncRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/ha-full-sync"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
