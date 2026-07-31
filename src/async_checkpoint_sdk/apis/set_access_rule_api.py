from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_rule_reply import AccessRuleReply
from async_checkpoint_sdk.models.access_rule_request_edit import AccessRuleRequestEdit
from config import Config


async def set_access_rule(
    client: ClientSession, data: AccessRuleRequestEdit, config: Config, **kwargs
) -> AccessRuleReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessRuleRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessRuleReply(**resp)
