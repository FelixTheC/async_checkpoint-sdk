from config import Config
from aiohttp import ClientSession
from models.mgcp_call_agent_reply import MgcpCallAgentReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_voip_domain_mgcp_call_agent(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> MgcpCallAgentReply:
    """
    Retrieve existing VoIP Domain MGCP Call Agent using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MgcpCallAgentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-voip-domain-mgcp-call-agent"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MgcpCallAgentReply(**resp)
