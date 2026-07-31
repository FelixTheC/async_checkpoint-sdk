from config import Config
from aiohttp import ClientSession
from models.automatic_purge_reply import AutomaticPurgeReply
from models.automatic_purge_request_show import AutomaticPurgeRequestShow


async def show_automatic_purge(
    client: ClientSession, data: AutomaticPurgeRequestShow, config: Config, **kwargs
) -> AutomaticPurgeReply:
    """
    Show Automatic Purge.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AutomaticPurgeRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutomaticPurgeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-automatic-purge"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AutomaticPurgeReply(**resp)
