from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_rule_reply import AccessRuleReply
from async_checkpoint_sdk.models.access_rule_request_new import AccessRuleRequestNew
from config import Config


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
