from config import Config
from aiohttp import ClientSession
from models.mgcp_call_agent_reply import MgcpCallAgentReply
from models.mgcp_call_agent_request_edit import MgcpCallAgentRequestEdit


async def clone_voip_domain_mgcp_call_agent(
    client: ClientSession, data: MgcpCallAgentRequestEdit, config: Config, **kwargs
) -> MgcpCallAgentReply:
    """
    Clone existing VoIP Domain MGCP Call Agent.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MgcpCallAgentRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MgcpCallAgentReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-voip-domain-mgcp-call-agent"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MgcpCallAgentReply(**resp)
