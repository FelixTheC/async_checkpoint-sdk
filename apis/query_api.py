from aiohttp import ClientSession

from config import Config
from models.cpm_query_reply import CpmQueryReply
from models.cpm_query_request import CpmQueryRequest


async def query(
    client: ClientSession, data: CpmQueryRequest, config: Config, **kwargs
) -> CpmQueryReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CpmQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CpmQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/query"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CpmQueryReply(**resp)
