from config import Config
from aiohttp import ClientSession
from models.mobile_profile_rule_reply import MobileProfileRuleReply
from models.mobile_profile_rule_identifier_request_show import (
    MobileProfileRuleIdentifierRequestShow,
)


async def show_mobile_access_profile_rule(
    client: ClientSession, data: MobileProfileRuleIdentifierRequestShow, config: Config, **kwargs
) -> MobileProfileRuleReply:
    """
    Retrieve existing Mobile Access Profile rule using rule number or uid or name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileRuleIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-mobile-access-profile-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileRuleReply(**resp)
