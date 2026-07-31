from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_applications_rule_reply import MobileApplicationsRuleReply
from async_checkpoint_sdk.models.mobile_applications_rule_request_new import (
    MobileApplicationsRuleRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_mobile_access_rule(
    client: ClientSession, data: MobileApplicationsRuleRequestNew, config: SDKConfig, **kwargs
) -> MobileApplicationsRuleReply:
    """
    Create new Mobile Access rule for associating groups of users with a available apps.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsRuleRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MobileApplicationsRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-mobile-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsRuleReply(**resp)
