from config import Config
from aiohttp import ClientSession
from models.global_properties_reply import GlobalPropertiesReply
from models.global_properties_request_edit import GlobalPropertiesRequestEdit


async def set_global_properties(
    client: ClientSession, data: GlobalPropertiesRequestEdit, config: Config, **kwargs
) -> GlobalPropertiesReply:
    """
    Edit Global Properties.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GlobalPropertiesRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GlobalPropertiesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-global-properties"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalPropertiesReply(**resp)
