from config import Config
from aiohttp import ClientSession
from models.show_logs_reply import ShowLogsReply
from models.show_logs_request import ShowLogsRequest


async def show_logs(
    client: ClientSession, data: ShowLogsRequest, config: Config, **kwargs
) -> ShowLogsReply:
    """
    Showing logs according to the given filter.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowLogsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShowLogsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-logs"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowLogsReply(**resp)
