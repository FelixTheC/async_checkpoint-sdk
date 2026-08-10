from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_applications_rule_identifier_request_show import (
    MobileApplicationsRuleIdentifierRequestShow,
)
from async_checkpoint_sdk.models.mobile_applications_rule_reply import MobileApplicationsRuleReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_mobile_access_rule(
    client: ClientSession,
    data: MobileApplicationsRuleIdentifierRequestShow,
    config: SDKConfig,
    **kwargs,
) -> MobileApplicationsRuleReply:
    """
    Retrieve existing Mobile Access rule using rule number or uid or name.

    Parameters
    ----------
    client : ClientSession
    data : MobileApplicationsRuleIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

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
