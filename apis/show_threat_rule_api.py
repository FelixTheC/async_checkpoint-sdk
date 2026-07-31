from config import Config
from aiohttp import ClientSession
from models.threat_rule_reply import ThreatRuleReply
from models.threat_rule_identifier_request import ThreatRuleIdentifierRequest


async def show_threat_rule(
    client: ClientSession, data: ThreatRuleIdentifierRequest, config: Config, **kwargs
) -> ThreatRuleReply:
    """
    Retrieve existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatRuleIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ThreatRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ThreatRuleReply(**resp)
