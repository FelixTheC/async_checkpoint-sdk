from aiohttp import ClientSession

from async_checkpoint_sdk.models.nat_rule_identifier_request_show import (
    NatRuleIdentifierRequestShow,
)
from async_checkpoint_sdk.models.nat_rule_reply import NatRuleReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_nat_rule(
    client: ClientSession, data: NatRuleIdentifierRequestShow, config: SDKConfig, **kwargs
) -> NatRuleReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : NatRuleIdentifierRequestShow
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    NatRuleReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-nat-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return NatRuleReply(**resp)
