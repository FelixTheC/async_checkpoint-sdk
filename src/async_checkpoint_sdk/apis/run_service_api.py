from aiohttp import ClientSession

from async_checkpoint_sdk.models.service_reply import ServiceReply
from async_checkpoint_sdk.models.service_request import ServiceRequest
from config import Config


async def run_service(
    client: ClientSession, data: ServiceRequest, config: Config, **kwargs
) -> ServiceReply:
    """
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ServiceRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ServiceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-service"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ServiceReply(**resp)
