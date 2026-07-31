from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_rule_reply import ThreatRuleReply
from async_checkpoint_sdk.models.threat_rule_request_edit import ThreatRuleRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_threat_rule(
    client: ClientSession, data: ThreatRuleRequestEdit, config: SDKConfig, **kwargs
) -> ThreatRuleReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatRuleRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-threat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatRuleReply(**resp)
