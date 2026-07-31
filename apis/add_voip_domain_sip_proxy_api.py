from aiohttp import ClientSession

from config import Config
from models.sip_proxy_reply import SipProxyReply
from models.sip_proxy_request_new import SipProxyRequestNew


async def add_voip_domain_sip_proxy(
    client: ClientSession, data: SipProxyRequestNew, config: Config, **kwargs
) -> SipProxyReply:
    """
    Create new VoIP Domain SIP Proxy.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : SipProxyRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SipProxyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-voip-domain-sip-proxy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SipProxyReply(**resp)
