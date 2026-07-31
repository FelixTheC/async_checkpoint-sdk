from config import Config
from aiohttp import ClientSession
from models.sccp_call_manager_reply import SccpCallManagerReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_voip_domain_sccp_call_manager(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> SccpCallManagerReply:
    """
    Retrieve existing VoIP Domain SCCP Call Manager using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SccpCallManagerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-voip-domain-sccp-call-manager"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SccpCallManagerReply(**resp)
