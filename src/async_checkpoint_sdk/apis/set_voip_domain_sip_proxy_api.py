from aiohttp import ClientSession

from async_checkpoint_sdk.models.sip_proxy_reply import SipProxyReply
from async_checkpoint_sdk.models.sip_proxy_request_edit import SipProxyRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_voip_domain_sip_proxy(
    client: ClientSession, data: SipProxyRequestEdit, config: SDKConfig, **kwargs
) -> SipProxyReply:
    """
    Edit existing VoIP Domain SIP Proxy using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : SipProxyRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SipProxyReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-voip-domain-sip-proxy"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SipProxyReply(**resp)
