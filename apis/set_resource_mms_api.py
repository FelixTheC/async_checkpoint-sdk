from aiohttp import ClientSession

from config import Config
from models.mms_resource_reply import MmsResourceReply
from models.mms_resource_request_edit import MmsResourceRequestEdit


async def set_resource_mms(
    client: ClientSession, data: MmsResourceRequestEdit, config: Config, **kwargs
) -> MmsResourceReply:
    """
    Edit existing MMS resource using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MmsResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MmsResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-mms"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MmsResourceReply(**resp)
