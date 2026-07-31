from aiohttp import ClientSession

from async_checkpoint_sdk.models.web_console_statistics_reply import WebConsoleStatisticsReply
from async_checkpoint_sdk.models.web_console_statistics_request import WebConsoleStatisticsRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_web_console_statistics(
    client: ClientSession, data: WebConsoleStatisticsRequest, config: SDKConfig, **kwargs
) -> WebConsoleStatisticsReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : WebConsoleStatisticsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    WebConsoleStatisticsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-web-console-statistics"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return WebConsoleStatisticsReply(**resp)
