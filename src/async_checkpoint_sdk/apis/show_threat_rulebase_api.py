from aiohttp import ClientSession

from async_checkpoint_sdk.models.query_threat_rulebase_reply import QueryThreatRulebaseReply
from async_checkpoint_sdk.models.query_threat_rulebase_request import QueryThreatRulebaseRequest
from config import Config


async def show_threat_rulebase(
    client: ClientSession, data: QueryThreatRulebaseRequest, config: Config, **kwargs
) -> QueryThreatRulebaseReply:
    """
    Shows the entire Threat Prevention Rules layer. The reply features a list of rules. Each rule has the Global Exceptions Group attached and may have any number of an Exceptions Group attached. An optional "filter" field may be added in order to filter out only those rules that match a search criteria.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : QueryThreatRulebaseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryThreatRulebaseReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-threat-rulebase"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryThreatRulebaseReply(**resp)
