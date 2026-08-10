from aiohttp import ClientSession

from async_checkpoint_sdk.models.t_l_s_rule_reply import TLSRuleReply
from async_checkpoint_sdk.models.t_l_s_rule_request_edit import TLSRuleRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_https_rule(
    client: ClientSession, data: TLSRuleRequestEdit, config: SDKConfig, **kwargs
) -> TLSRuleReply:
    """
    Edit existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : TLSRuleRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    TLSRuleReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-https-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSRuleReply(**resp)
