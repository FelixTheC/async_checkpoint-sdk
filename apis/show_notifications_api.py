from aiohttp import ClientSession

from config import Config
from models.notification_query_reply import NotificationQueryReply
from models.notification_query_request import NotificationQueryRequest


async def show_notifications(
    client: ClientSession, data: NotificationQueryRequest, config: Config, **kwargs
) -> NotificationQueryReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NotificationQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NotificationQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-notifications"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NotificationQueryReply(**resp)
