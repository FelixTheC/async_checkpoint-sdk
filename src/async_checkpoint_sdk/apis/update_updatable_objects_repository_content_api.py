from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.empty_request import EmptyRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def update_updatable_objects_repository_content(
    client: ClientSession, data: EmptyRequest, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Updates the content of the Updatable Objects repository from the Check Point User Center.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    data : EmptyRequest [Argument]
        data : EmptyRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = (
        f"https://{config.server}:{config.port}/web_api/update-updatable-objects-repository-content"
    )
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
