from aiohttp import ClientSession

from async_checkpoint_sdk.models.sccp_call_manager_reply import SccpCallManagerReply
from async_checkpoint_sdk.models.sccp_call_manager_request_edit import SccpCallManagerRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_voip_domain_sccp_call_manager(
    client: ClientSession, data: SccpCallManagerRequestEdit, config: SDKConfig, **kwargs
) -> SccpCallManagerReply:
    """
    Edit existing VoIP Domain SCCP Call Manager using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : SccpCallManagerRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SccpCallManagerReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-voip-domain-sccp-call-manager"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SccpCallManagerReply(**resp)
