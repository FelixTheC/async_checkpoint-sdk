from config import Config
from aiohttp import ClientSession
from models.cifs_resource_reply import CifsResourceReply
from models.cifs_resource_request_new import CifsResourceRequestNew


async def add_resource_cifs(
    client: ClientSession, data: CifsResourceRequestNew, config: Config, **kwargs
) -> CifsResourceReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CifsResourceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CifsResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-cifs"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CifsResourceReply(**resp)
