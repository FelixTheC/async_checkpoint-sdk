from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.notification_unsubscribe_request import NotificationUnsubscribeRequest


async def unsubscribe_notification(
    client: ClientSession, data: NotificationUnsubscribeRequest, config: Config, **kwargs
) -> ApiOkReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : NotificationUnsubscribeRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/unsubscribe-notification"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
