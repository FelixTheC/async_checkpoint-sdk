from aiohttp import ClientSession

from async_checkpoint_sdk.models.query_threat_exception_rulebase_reply import (
    QueryThreatExceptionRulebaseReply,
)
from async_checkpoint_sdk.models.query_threat_exception_rulebase_request import (
    QueryThreatExceptionRulebaseRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_threat_rule_exception_rulebase(
    client: ClientSession, data: QueryThreatExceptionRulebaseRequest, config: SDKConfig, **kwargs
) -> QueryThreatExceptionRulebaseReply:
    """
    Shows the entire Threat Exceptions layer  generated for a given threat rule.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : QueryThreatExceptionRulebaseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryThreatExceptionRulebaseReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-rule-exception-rulebase"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryThreatExceptionRulebaseReply(**resp)
