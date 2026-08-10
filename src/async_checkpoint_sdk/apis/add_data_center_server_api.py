from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_center_server_request_new import DataCenterServerRequestNew
from async_checkpoint_sdk.models.data_center_server_task_reply import DataCenterServerTaskReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_data_center_server(
    client: ClientSession, data: DataCenterServerRequestNew, config: SDKConfig, **kwargs
) -> DataCenterServerTaskReply:
    """
    Create new Data Center Server.<br> Data Center Server represents the connection to a cloud environment.<br>
    The Data Center Server contains Data Center Objects, these objects can be imported from it using the add-data-center-object command.
    <span class="show-only-in-doc-ui"><br><span class="show-only-in-doc-ui"><span style="color: red;">Note:</span>
    Each Data Center Server type uses additional dedicated arguments, <a data-toggle="modal" href="#" data-target="#DataC
    Parameters
    ----------
    client : ClientSession
        data : DataCenterServerRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterServerTaskReply.
    data : DataCenterServerRequestNew
        data : DataCenterServerRequestNew [Argument].
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    DataCenterServerTaskReply

    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-center-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterServerTaskReply(**resp)
