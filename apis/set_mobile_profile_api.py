from aiohttp import ClientSession

from config import Config
from models.mobile_profile_reply import MobileProfileReply
from models.mobile_profile_request_edit import MobileProfileRequestEdit


async def set_mobile_profile(
    client: ClientSession, data: MobileProfileRequestEdit, config: Config, **kwargs
) -> MobileProfileReply:
    """
    Edit existing Mobile Profile using name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-mobile-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileReply(**resp)
