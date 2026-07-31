from aiohttp import ClientSession

from config import Config
from models.ad_group_reply import AdGroupReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_ad_group(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> AdGroupReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AdGroupReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-ad-group"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AdGroupReply(**resp)
