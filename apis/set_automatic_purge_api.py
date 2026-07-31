from aiohttp import ClientSession

from config import Config
from models.automatic_purge_reply import AutomaticPurgeReply
from models.automatic_purge_request import AutomaticPurgeRequest


async def set_automatic_purge(
    client: ClientSession, data: AutomaticPurgeRequest, config: Config, **kwargs
) -> AutomaticPurgeReply:
    """
        Set Automatic Purge. NOTE! this command will permanently delete all of the data which belongs to the published sessions not selected for preservation.
    In Multi-Domain Server, it should be done for each domain.
    
    Parameters
    ----------
    client : ClientSession [Argument]
        data : AutomaticPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutomaticPurgeReply
    data : AutomaticPurgeRequest [Argument]
        data : AutomaticPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutomaticPurgeReply
    data : AutomaticPurgeRequest [Argument]
        data : AutomaticPurgeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AutomaticPurgeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-automatic-purge"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AutomaticPurgeReply(**resp)
