from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)
from async_checkpoint_sdk.models.data_center_query_reply import DataCenterQueryReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_data_center_query(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: SDKConfig, **kwargs
) -> DataCenterQueryReply:
    """
    Retrieves data center query.

    Parameters
    ----------
    client : ClientSession [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
        data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    DataCenterQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-data-center-query"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return DataCenterQueryReply(**resp)
