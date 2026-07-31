from config import Config
from aiohttp import ClientSession
from models.query_access_rulebase_request import QueryAccessRulebaseRequest
from models.query_access_rulebase_reply import QueryAccessRulebaseReply


async def show_access_rulebase(
    client: ClientSession, data: QueryAccessRulebaseRequest, config: Config, **kwargs
) -> QueryAccessRulebaseReply:
    """
    Shows the entire Access Rules layer.  This layer is divided into sections. An Access Rule may be within a section, or independent of a section (in which case it is said to be under the "global" section). The reply features a list of objects. Each object may be a section of the layer, with all its rules in, or a rule itself, for the case of rules which are under the global section. An optional "filter" field may be added in order to filter out only those rules that match a search criteria.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : QueryAccessRulebaseRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    QueryAccessRulebaseReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-access-rulebase"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryAccessRulebaseReply(**resp)
