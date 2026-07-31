from config import Config
from aiohttp import ClientSession
from models.show_fwm_sid_reply import ShowFwmSidReply
from models.show_fwm_sid_request import ShowFwmSidRequest


async def show_fwm_sid(
    client: ClientSession, data: ShowFwmSidRequest, config: Config, **kwargs
) -> ShowFwmSidReply:
    """ 
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ShowFwmSidRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ShowFwmSidReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-fwm-sid"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ShowFwmSidReply(**resp)
