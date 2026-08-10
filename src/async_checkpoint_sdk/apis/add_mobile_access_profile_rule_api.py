from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_profile_rule_reply import MobileProfileRuleReply
from async_checkpoint_sdk.models.mobile_profile_rule_request_new import MobileProfileRuleRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_mobile_access_profile_rule(
    client: ClientSession, data: MobileProfileRuleRequestNew, config: SDKConfig, **kwargs
) -> MobileProfileRuleReply:
    """
    Create new Mobile Access Profile rule for associating groups of users with a profile configuration.

    Parameters
    ----------
    client : ClientSession
    data : MobileProfileRuleRequestNew
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileRuleReply
    config : Config [Argument]
        data : MobileProfileRuleRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileRuleReply
    config : Config [Argument]
        data : MobileProfileRuleRequestNew [Argument]
        config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileProfileRuleReply.
    config : SDKConfig
        data : MobileProfileRuleRequestNew [Argument]
        config : Config [Argument].
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MobileProfileRuleReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-mobile-access-profile-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileProfileRuleReply(**resp)
