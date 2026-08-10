from aiohttp import ClientSession

from async_checkpoint_sdk.models.locking_reply import LockingReply
from async_checkpoint_sdk.models.locking_request import LockingRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def unlock_object(
    client: ClientSession, data: LockingRequest, config: SDKConfig, **kwargs
) -> LockingReply:
    """
        Unlock object using uid or {name and type}.
    Can unlock object only if the current session owns the lock and there are no changes on the object.

    Parameters
    ----------
    client : ClientSession
    data : LockingRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    LockingReply

    """
    url = f"https://{config.server}:{config.port}/web_api/unlock-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LockingReply(**resp)
