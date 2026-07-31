from aiohttp import ClientSession

from async_checkpoint_sdk.models.azure_a_d_request_new import AzureADRequestNew
from async_checkpoint_sdk.models.azure_a_d_task_reply import AzureADTaskReply
from config import Config


async def add_azure_ad(
    client: ClientSession, data: AzureADRequestNew, config: Config, **kwargs
) -> AzureADTaskReply:
    """
    Create a new Microsoft Entra ID object (formerly, Azure AD). <br>Microsoft Entra ID is Microsoft's cloud-based identity and access management service.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AzureADRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AzureADTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-azure-ad"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AzureADTaskReply(**resp)
