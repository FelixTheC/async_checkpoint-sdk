from aiohttp import ClientSession

from config import Config
from models.global_properties_reply import GlobalPropertiesReply
from models.global_properties_request_show import GlobalPropertiesRequestShow


async def show_global_properties(
    client: ClientSession, data: GlobalPropertiesRequestShow, config: Config, **kwargs
) -> GlobalPropertiesReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GlobalPropertiesRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GlobalPropertiesReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-global-properties"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GlobalPropertiesReply(**resp)
