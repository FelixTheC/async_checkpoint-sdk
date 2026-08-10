from aiohttp import ClientSession

from async_checkpoint_sdk.models.nat_rule_reply import NatRuleReply
from async_checkpoint_sdk.models.nat_rule_request_new import NatRuleRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_nat_rule(
    client: ClientSession, data: NatRuleRequestNew, config: SDKConfig, **kwargs
) -> NatRuleReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession
    data : NatRuleRequestNew
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NatRuleReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-nat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NatRuleReply(**resp)
