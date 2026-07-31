from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.threat_rule_identifier_request import ThreatRuleIdentifierRequest


async def delete_threat_rule(
    client: ClientSession, data: ThreatRuleIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ThreatRuleIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-threat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
