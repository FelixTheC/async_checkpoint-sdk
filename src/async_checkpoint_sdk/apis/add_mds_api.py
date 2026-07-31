from aiohttp import ClientSession

from async_checkpoint_sdk.models.mds_reply import MdsReply
from async_checkpoint_sdk.models.mds_request_new import MdsRequestNew
from config import Config


async def add_mds(client: ClientSession, data: MdsRequestNew, config: Config, **kwargs) -> MdsReply:
    """
    Create new object of type Multi-Domain Server or Multi-Domain Log Server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MdsRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MdsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-mds"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdsReply(**resp)
