from aiohttp import ClientSession

from async_checkpoint_sdk.models.cloud_services_request_edit import CloudServicesRequestEdit
from async_checkpoint_sdk.models.cloud_services_status_reply import CloudServicesStatusReply
from config import Config


async def set_cloud_services(
    client: ClientSession, data: CloudServicesRequestEdit, config: Config, **kwargs
) -> CloudServicesStatusReply:
    """
    Set the connection settings between the Management Server and Check Point's Infinity Portal.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudServicesRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CloudServicesStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-cloud-services"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CloudServicesStatusReply(**resp)
