from aiohttp import ClientSession

from async_checkpoint_sdk.models.uri_for_qos_resource_reply import UriForQosResourceReply
from async_checkpoint_sdk.models.uri_for_qos_resource_request_edit import (
    UriForQosResourceRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_resource_uri_for_qos(
    client: ClientSession, data: UriForQosResourceRequestEdit, config: SDKConfig, **kwargs
) -> UriForQosResourceReply:
    """
    Edit existing Uri For QoS resource using object name or uid.

    Parameters
    ----------
    client : ClientSession
    data : UriForQosResourceRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    UriForQosResourceReply

    """
    url = f"https://{config.server}:{config.port}/web_api/set-resource-uri-for-qos"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriForQosResourceReply(**resp)
