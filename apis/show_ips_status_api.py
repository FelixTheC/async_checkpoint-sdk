from config import Config
from aiohttp import ClientSession
from models.ips_status_request import IpsStatusRequest
from models.ips_status_reply import IpsStatusReply


async def show_ips_status(
    client: ClientSession, data: IpsStatusRequest, config: Config, **kwargs
) -> IpsStatusReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : IpsStatusRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    IpsStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ips-status"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return IpsStatusReply(**resp)
