from aiohttp import ClientSession

from config import Config
from models.api_ok_reply import ApiOkReply
from models.compliance_gaia_best_practice_request_delete import (
    ComplianceGaiaBestPracticeRequestDelete,
)


async def delete_gaia_best_practice(
    client: ClientSession, data: ComplianceGaiaBestPracticeRequestDelete, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete a user-defined Gaia Best Practice.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ComplianceGaiaBestPracticeRequestDelete [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-gaia-best-practice"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
