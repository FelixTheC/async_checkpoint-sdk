from aiohttp import ClientSession

from async_checkpoint_sdk.models.sccp_call_manager_reply import SccpCallManagerReply
from async_checkpoint_sdk.models.sccp_call_manager_request_new import SccpCallManagerRequestNew
from config import Config


async def add_voip_domain_sccp_call_manager(
    client: ClientSession, data: SccpCallManagerRequestNew, config: Config, **kwargs
) -> SccpCallManagerReply:
    """
    Create new VoIP Domain SCCP Call Manager.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SccpCallManagerRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SccpCallManagerReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-voip-domain-sccp-call-manager"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SccpCallManagerReply(**resp)
