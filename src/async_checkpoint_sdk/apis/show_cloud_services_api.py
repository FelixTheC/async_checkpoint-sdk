from aiohttp import ClientSession

from async_checkpoint_sdk.models.cloud_services_request_show import CloudServicesRequestShow
from async_checkpoint_sdk.models.cloud_services_status_reply import CloudServicesStatusReply
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cloud_services(
    client: ClientSession, data: CloudServicesRequestShow, config: SDKConfig, **kwargs
) -> CloudServicesStatusReply:
    """
    Show the connection status of the Management Server to Check Point's Infinity Portal.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudServicesRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CloudServicesStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cloud-services"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CloudServicesStatusReply(**resp)
