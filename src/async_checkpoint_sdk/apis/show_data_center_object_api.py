from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_center_object_reply import DataCenterObjectReply
from async_checkpoint_sdk.models.data_center_object_request_show import DataCenterObjectRequestShow
from config import Config


async def show_data_center_object(
    client: ClientSession, data: DataCenterObjectRequestShow, config: Config, **kwargs
) -> DataCenterObjectReply:
    """
    Retrieve existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : DataCenterObjectRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-data-center-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterObjectReply(**resp)
