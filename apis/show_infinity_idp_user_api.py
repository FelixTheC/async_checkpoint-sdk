from config import Config
from aiohttp import ClientSession
from models.infinity_idp_user_reply import InfinityIdpUserReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_infinity_idp_user(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> InfinityIdpUserReply:
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
    InfinityIdpUserReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-infinity-idp-user"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return InfinityIdpUserReply(**resp)
