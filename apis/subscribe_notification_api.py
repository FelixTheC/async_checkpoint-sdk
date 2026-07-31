from aiohttp import ClientSession

from config import Config
from models.notification_subscribe_reply import NotificationSubscribeReply
from models.notification_subscribe_request import NotificationSubscribeRequest


async def subscribe_notification(
    client: ClientSession, data: NotificationSubscribeRequest, config: Config, **kwargs
) -> NotificationSubscribeReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NotificationSubscribeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    NotificationSubscribeReply
    """
    url = f"https://{config.server}:{config.port}/web_api/subscribe-notification"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NotificationSubscribeReply(**resp)
