from config import Config
from aiohttp import ClientSession
from models.cloud_services_status_reply import CloudServicesStatusReply
from models.cloud_connect_mgmt_request import CloudConnectMgmtRequest


async def connect_cloud_services(
    client: ClientSession, data: CloudConnectMgmtRequest, config: Config, **kwargs
) -> CloudServicesStatusReply:
    """
    Securely connect the Management Server to Check Point's Infinity Portal. <br>This is a preliminary operation so that the management server can use various Check Point cloud-based security services hosted in the Infinity Portal.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloudConnectMgmtRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CloudServicesStatusReply
    """
    url = f"https://{config.server}:{config.port}/web_api/connect-cloud-services"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CloudServicesStatusReply(**resp)
