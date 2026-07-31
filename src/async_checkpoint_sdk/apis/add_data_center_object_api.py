from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_center_object_reply import DataCenterObjectReply
from async_checkpoint_sdk.models.data_center_object_request_new import DataCenterObjectRequestNew
from config import Config


async def add_data_center_object(
    client: ClientSession, data: DataCenterObjectRequestNew, config: Config, **kwargs
) -> DataCenterObjectReply:
    """
    Create new object.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DataCenterObjectRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-data-center-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterObjectReply(**resp)
