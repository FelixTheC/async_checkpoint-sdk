from config import Config
from models.mobile_applications_rule_reply import MobileApplicationsRuleReply
from models.mobile_applications_rule_identifier_request_show import (
    MobileApplicationsRuleIdentifierRequestShow,
)
from aiohttp import ClientSession


async def show_mobile_access_rule(
    client: ClientSession,
    data: MobileApplicationsRuleIdentifierRequestShow,
    config: Config,
    **kwargs,
) -> MobileApplicationsRuleReply:
    """
    Retrieve existing Mobile Access rule using rule number or uid or name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsRuleIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileApplicationsRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-mobile-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsRuleReply(**resp)
