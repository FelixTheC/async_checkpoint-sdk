from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_rule_identifier_request_show import (
    AccessRuleIdentifierRequestShow,
)
from async_checkpoint_sdk.models.access_rule_reply import AccessRuleReply
from config import Config


async def show_access_rule(
    client: ClientSession, data: AccessRuleIdentifierRequestShow, config: Config, **kwargs
) -> AccessRuleReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AccessRuleIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AccessRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AccessRuleReply(**resp)
