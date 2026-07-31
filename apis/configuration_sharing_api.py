from config import Config
from aiohttp import ClientSession
from models.sho_request import ShoRequest
from models.sho_reply import ShoReply


async def configuration_sharing(
    client: ClientSession, data: ShoRequest, config: Config, **kwargs
) -> ShoReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShoRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShoReply
    """
    url = f"https://{config.server}:{config.port}/web_api/configuration-sharing"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShoReply(**resp)
