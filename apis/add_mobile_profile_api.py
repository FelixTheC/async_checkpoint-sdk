from config import Config
from aiohttp import ClientSession
from models.mobile_profile_reply import MobileProfileReply
from models.mobile_profile_request_new import MobileProfileRequestNew


async def add_mobile_profile(
    client: ClientSession, data: MobileProfileRequestNew, config: Config, **kwargs
) -> MobileProfileReply:
    """
    Create new Mobile Profile.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-mobile-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileReply(**resp)
