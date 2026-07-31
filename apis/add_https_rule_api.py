from aiohttp import ClientSession

from config import Config
from models.t_l_s_rule_reply import TLSRuleReply
from models.t_l_s_rule_request_new import TLSRuleRequestNew


async def add_https_rule(
    client: ClientSession, data: TLSRuleRequestNew, config: Config, **kwargs
) -> TLSRuleReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TLSRuleRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    TLSRuleReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-https-rule"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return TLSRuleReply(**resp)
