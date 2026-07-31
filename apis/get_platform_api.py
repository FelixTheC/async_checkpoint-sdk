from config import Config
from aiohttp import ClientSession
from models.get_platform_reply import GetPlatformReply
from models.get_platform_request import GetPlatformRequest


async def get_platform(
    client: ClientSession, data: GetPlatformRequest, config: Config, **kwargs
) -> GetPlatformReply:
    """
    Get actual platform (Hardware, Version, OS) from gateway, cluster or Check Point host, and update the object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : GetPlatformRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    GetPlatformReply
    """
    url = f"https://{config.server}:{config.port}/web_api/get-platform"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return GetPlatformReply(**resp)
