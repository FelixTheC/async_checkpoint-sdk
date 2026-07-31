from aiohttp import ClientSession

from async_checkpoint_sdk.models.uri_for_qos_resource_reply import UriForQosResourceReply
from async_checkpoint_sdk.models.uri_for_qos_resource_request_new import (
    UriForQosResourceRequestNew,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_resource_uri_for_qos(
    client: ClientSession, data: UriForQosResourceRequestNew, config: SDKConfig, **kwargs
) -> UriForQosResourceReply:
    """
    Create new Uri For QoS resource.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : UriForQosResourceRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UriForQosResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-resource-uri-for-qos"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriForQosResourceReply(**resp)
