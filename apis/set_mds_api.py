from config import Config
from aiohttp import ClientSession
from models.mds_request_edit import MdsRequestEdit
from models.mds_reply import MdsReply


async def set_mds(
    client: ClientSession, data: MdsRequestEdit, config: Config, **kwargs
) -> MdsReply:
    """
    Edit existing object of type Multi-Domain Server or Multi-Domain Log Server using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MdsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MdsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-mds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsReply(**resp)
