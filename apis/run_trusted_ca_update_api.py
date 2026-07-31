from config import Config
from aiohttp import ClientSession
from models.api_task_reply import ApiTaskReply
from models.trusted_ca_update_request import TrustedCaUpdateRequest


async def run_trusted_ca_update(
    client: ClientSession, data: TrustedCaUpdateRequest, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Executes Trusted CAs package update.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : TrustedCaUpdateRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/run-trusted-ca-update"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
