from config import Config
from aiohttp import ClientSession
from models.cifs_resource_request_edit import CifsResourceRequestEdit
from models.cifs_resource_reply import CifsResourceReply


async def set_resource_cifs(
    client: ClientSession, data: CifsResourceRequestEdit, config: Config, **kwargs
) -> CifsResourceReply:
    """
    Edit existing object using object name or uid.
    
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
    url = f"https://{config.server}:{config.port}/web_api/set-resource-cifs"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CifsResourceReply(**resp)
