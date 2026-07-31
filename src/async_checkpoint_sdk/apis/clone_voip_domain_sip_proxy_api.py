from aiohttp import ClientSession

from async_checkpoint_sdk.models.sip_proxy_reply import SipProxyReply
from async_checkpoint_sdk.models.sip_proxy_request_edit import SipProxyRequestEdit
from config import Config


async def clone_voip_domain_sip_proxy(
    client: ClientSession, data: SipProxyRequestEdit, config: Config, **kwargs
) -> SipProxyReply:
    """
    Clone existing VoIP Domain SIP Proxy.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SipProxyRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SipProxyReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-voip-domain-sip-proxy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SipProxyReply(**resp)
