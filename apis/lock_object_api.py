from aiohttp import ClientSession

from config import Config
from models.locking_reply import LockingReply
from models.locking_request import LockingRequest


async def lock_object(
    client: ClientSession, data: LockingRequest, config: Config, **kwargs
) -> LockingReply:
    """
        Lock object using uid or {name and type}.
    Can lock object only if the object is not locked by another session.
     The object can be unlocked by the following commands: unlock, publish or discard.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : LockingRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    LockingReply
    """
    url = f"https://{config.server}:{config.port}/web_api/lock-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return LockingReply(**resp)
