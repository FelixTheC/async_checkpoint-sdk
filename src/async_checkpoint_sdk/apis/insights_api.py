from aiohttp import ClientSession

from async_checkpoint_sdk.models.autonomous_firewall_reply import AutonomousFirewallReply
from async_checkpoint_sdk.models.autonomous_firewall_request import AutonomousFirewallRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def insights(
    client: ClientSession, data: AutonomousFirewallRequest, config: SDKConfig, **kwargs
) -> AutonomousFirewallReply:
    """
    TBD.

    Parameters
    ----------
    client : ClientSession
    data : AutonomousFirewallRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    AutonomousFirewallReply

    """
    url = f"https://{config.server}:{config.port}/web_api/insights"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AutonomousFirewallReply(**resp)
