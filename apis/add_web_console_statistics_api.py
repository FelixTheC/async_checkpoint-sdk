from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.web_console_statistics_request_new import WebConsoleStatisticsRequestNew


async def add_web_console_statistics(
    client: ClientSession, data: WebConsoleStatisticsRequestNew, config: Config, **kwargs
) -> ApiOkReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebConsoleStatisticsRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-web-console-statistics"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
