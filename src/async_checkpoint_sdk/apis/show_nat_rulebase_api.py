from aiohttp import ClientSession

from async_checkpoint_sdk.models.query_nat_rulebase_reply import QueryNatRulebaseReply
from async_checkpoint_sdk.models.query_nat_rulebase_request import QueryNatRulebaseRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_nat_rulebase(
    client: ClientSession, data: QueryNatRulebaseRequest, config: SDKConfig, **kwargs
) -> QueryNatRulebaseReply:
    """
    Shows the entire NAT Rules layer.  This layer is divided into sections. A NAT Rule may be within a section, or independent of a section (in which case it is said to be under the "global" section). There are two types of sections: auto generated read only sections and general sections which are created manually. The reply features a list of objects. Each object may be a section of the layer, within which its rules may be found, or a rule itself, for the case of rules which are under the global section. An optional "filter" field may be added in order to filter out only those rules that match a search criteria.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : QueryNatRulebaseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryNatRulebaseReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-nat-rulebase"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryNatRulebaseReply(**resp)
