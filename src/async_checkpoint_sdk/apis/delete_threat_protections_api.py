from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.delete_protections_request import DeleteProtectionsRequest
from config import Config


async def delete_threat_protections(
    client: ClientSession, data: DeleteProtectionsRequest, config: Config, **kwargs
) -> ApiTaskReply:
    """
    Deletes threat protections.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DeleteProtectionsRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-threat-protections"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
