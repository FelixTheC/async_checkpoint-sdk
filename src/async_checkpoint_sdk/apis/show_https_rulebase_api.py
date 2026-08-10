from aiohttp import ClientSession

from async_checkpoint_sdk.models.query_t_l_s_inspection_rulebase_reply import (
    QueryTLSInspectionRulebaseReply,
)
from async_checkpoint_sdk.models.query_t_l_s_inspection_rulebase_request import (
    QueryTLSInspectionRulebaseRequest,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_https_rulebase(
    client: ClientSession, data: QueryTLSInspectionRulebaseRequest, config: SDKConfig, **kwargs
) -> QueryTLSInspectionRulebaseReply:
    """
    Shows the entire HTTPS Inspection Rules layer.  This layer is divided into sections. An HTTPS Inspection Rule may be within a section, or independent of a section (in which case it is said to be under the "global" section). The reply features a list of objects. Each object may be a section of the layer, with all its rules in, or a rule itself, for the case of rules which are under the global section. An optional "filter" field may be added in order to filter out only those rules that match a search criteria.

    Parameters
    ----------
    client : ClientSession
    data : QueryTLSInspectionRulebaseRequest
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    QueryTLSInspectionRulebaseReply

    """
    url = f"https://{config.server}:{config.port}/web_api/show-https-rulebase"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return QueryTLSInspectionRulebaseReply(**resp)
