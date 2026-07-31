from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_tasks_reply import ApiTasksReply
from async_checkpoint_sdk.models.local_domain_request_new import LocalDomainRequestNew
from config import Config


async def add_domain(
    client: ClientSession, data: LocalDomainRequestNew, config: Config, **kwargs
) -> ApiTasksReply:
    """
    Create a new domain in a Multi-Domain-Management environment. In order to allow administrators to connect to this domain using SmartConsole, use add-trusted-client command.<br> Note: This operation is not part of session and will take effect immediately.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : LocalDomainRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTasksReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-domain"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTasksReply(**resp)
