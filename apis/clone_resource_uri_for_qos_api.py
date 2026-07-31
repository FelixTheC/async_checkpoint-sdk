from config import Config
from aiohttp import ClientSession
from models.uri_for_qos_resource_request_edit import UriForQosResourceRequestEdit
from models.uri_for_qos_resource_reply import UriForQosResourceReply


async def clone_resource_uri_for_qos(
    client: ClientSession, data: UriForQosResourceRequestEdit, config: Config, **kwargs
) -> UriForQosResourceReply:
    """
    Clone existing Uri For QoS resource.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UriForQosResourceRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UriForQosResourceReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-resource-uri-for-qos"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UriForQosResourceReply(**resp)
