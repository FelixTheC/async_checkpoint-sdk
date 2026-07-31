from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.mobile_applications_rule_identifier_request_show import (
    MobileApplicationsRuleIdentifierRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_mobile_access_rule(
    client: ClientSession,
    data: MobileApplicationsRuleIdentifierRequestShow,
    config: SDKConfig,
    **kwargs,
) -> ApiOkReply:
    """
    Delete existing Mobile Access rule using rule number or uid or name.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : MobileApplicationsRuleIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-mobile-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
