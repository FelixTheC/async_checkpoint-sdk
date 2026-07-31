from config import Config
from aiohttp import ClientSession
from models.access_rule_reply import AccessRuleReply
from models.access_rule_request_new import AccessRuleRequestNew


async def add_access_rule(
    client: ClientSession, data: AccessRuleRequestNew, config: Config, **kwargs
) -> AccessRuleReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessRuleRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessRuleReply(**resp)
