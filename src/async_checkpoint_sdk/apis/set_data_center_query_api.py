from aiohttp import ClientSession

from async_checkpoint_sdk.models.data_center_query_reply import DataCenterQueryReply
from async_checkpoint_sdk.models.data_center_query_request_edit import DataCenterQueryRequestEdit
from config import Config


async def set_data_center_query(
    client: ClientSession, data: DataCenterQueryRequestEdit, config: Config, **kwargs
) -> DataCenterQueryReply:
    """
    Edit existing data center query.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : DataCenterQueryRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    data : DataCenterQueryRequestEdit [Argument]
        data : DataCenterQueryRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    data : DataCenterQueryRequestEdit [Argument]
        data : DataCenterQueryRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-data-center-query"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterQueryReply(**resp)
