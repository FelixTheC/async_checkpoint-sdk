from aiohttp import ClientSession

from config import Config
from models.data_center_object_reply import DataCenterObjectReply
from models.data_center_object_request_edit import DataCenterObjectRequestEdit


async def set_data_center_object(
    client: ClientSession, data: DataCenterObjectRequestEdit, config: Config, **kwargs
) -> DataCenterObjectReply:
    """
    Edit existing object using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : DataCenterObjectRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterObjectReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-center-object"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterObjectReply(**resp)
