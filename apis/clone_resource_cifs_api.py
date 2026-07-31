from aiohttp import ClientSession

from config import Config
from models.cifs_resource_reply import CifsResourceReply
from models.cifs_resource_request_edit import CifsResourceRequestEdit


async def clone_resource_cifs(
    client: ClientSession, data: CifsResourceRequestEdit, config: Config, **kwargs
) -> CifsResourceReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CifsResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CifsResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-cifs"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CifsResourceReply(**resp)
