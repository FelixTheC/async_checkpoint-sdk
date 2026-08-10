from aiohttp import ClientSession

from async_checkpoint_sdk.models.mgcp_call_agent_reply import MgcpCallAgentReply
from async_checkpoint_sdk.models.mgcp_call_agent_request_edit import MgcpCallAgentRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_voip_domain_mgcp_call_agent(
    client: ClientSession, data: MgcpCallAgentRequestEdit, config: SDKConfig, **kwargs
) -> MgcpCallAgentReply:
    """
    Clone existing VoIP Domain MGCP Call Agent.

    Parameters
    ----------
    client : ClientSession
    data : MgcpCallAgentRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
