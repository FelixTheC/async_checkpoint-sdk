from config import Config
from aiohttp import ClientSession
from models.compliance_show_best_practice_query_reply import ComplianceShowBestPracticeQueryReply
from models.compliance_show_best_practice_query_request import (
    ComplianceShowBestPracticeQueryRequest,
)


async def show_best_practices(
    client: ClientSession, data: ComplianceShowBestPracticeQueryRequest, config: Config, **kwargs
) -> ComplianceShowBestPracticeQueryReply:
    """
    Retrieve all Best Practices.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceShowBestPracticeQueryRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ComplianceShowBestPracticeQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-best-practices"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ComplianceShowBestPracticeQueryReply(**resp)
