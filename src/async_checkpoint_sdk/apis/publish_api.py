from aiohttp import ClientSession

from async_checkpoint_sdk.models.publish_reply import PublishReply
from async_checkpoint_sdk.models.publish_request import PublishRequest
from config import Config


async def publish(
    client: ClientSession, data: PublishRequest, config: Config, **kwargs
) -> PublishReply:
    """
    All the changes done by this user will be seen by all users only after publish is called.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : PublishRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    PublishReply
    """
    url = f"https://{config.server}:{config.port}/web_api/publish"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return PublishReply(**resp)
