from config import Config
from aiohttp import ClientSession
from models.api_ok_reply import ApiOkReply
from models.mobile_profile_rule_identifier_request_show import (
    MobileProfileRuleIdentifierRequestShow,
)


async def delete_mobile_access_profile_rule(
    client: ClientSession, data: MobileProfileRuleIdentifierRequestShow, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing Mobile Access Profile rule using rule number or uid or name.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileProfileRuleIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-mobile-access-profile-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
