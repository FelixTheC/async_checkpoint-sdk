from aiohttp import ClientSession

from async_checkpoint_sdk.models.access_rule_identifier_request import AccessRuleIdentifierRequest
from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_access_rule(
    client: ClientSession, data: AccessRuleIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Delete existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : AccessRuleIdentifierRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-access-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
