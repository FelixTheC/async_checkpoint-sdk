from aiohttp import ClientSession

from async_checkpoint_sdk.models.mobile_applications_rule_reply import MobileApplicationsRuleReply
from async_checkpoint_sdk.models.mobile_applications_rule_request_edit import (
    MobileApplicationsRuleRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_mobile_access_rule(
    client: ClientSession, data: MobileApplicationsRuleRequestEdit, config: SDKConfig, **kwargs
) -> MobileApplicationsRuleReply:
    """
    Edit existing Mobile Access rule using rule number or uid or name.

    Parameters
    ----------
    client : ClientSession
    data : MobileApplicationsRuleRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    MobileApplicationsRuleReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-mobile-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MobileApplicationsRuleReply(**resp)
