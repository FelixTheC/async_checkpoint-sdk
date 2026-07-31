from aiohttp import ClientSession

from async_checkpoint_sdk.models.threat_rule_reply import ThreatRuleReply
from async_checkpoint_sdk.models.threat_rule_request_new import ThreatRuleRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_threat_rule(
    client: ClientSession, data: ThreatRuleRequestNew, config: SDKConfig, **kwargs
) -> ThreatRuleReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatRuleRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-threat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatRuleReply(**resp)
