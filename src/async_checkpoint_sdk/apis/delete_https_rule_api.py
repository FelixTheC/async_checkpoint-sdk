from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.t_l_s_rule_identifier_request import TLSRuleIdentifierRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def delete_https_rule(
    client: ClientSession, data: TLSRuleIdentifierRequest, config: SDKConfig, **kwargs
) -> ApiOkReply:
    """
    Delete existing HTTPS Inspection rule using rule number or uid.

    Parameters
    ----------
    client : ClientSession
    data : TLSRuleIdentifierRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    ApiOkReply

    """
    url = f"https://{config.server}:{config.port}/web_api/delete-https-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
