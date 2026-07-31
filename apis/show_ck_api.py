from aiohttp import ClientSession

from config import Config
from models.ck_reply import CkReply
from models.empty_request import EmptyRequest


async def show_ck(client: ClientSession, data: EmptyRequest, config: Config, **kwargs) -> CkReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ck"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CkReply(**resp)
