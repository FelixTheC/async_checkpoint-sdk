from aiohttp import ClientSession

from async_checkpoint_sdk.models.azure_a_d_content_query_reply import AzureADContentQueryReply
from async_checkpoint_sdk.models.azure_a_d_content_request import AzureADContentRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_azure_ad_content(
    client: ClientSession, data: AzureADContentRequest, config: SDKConfig, **kwargs
) -> AzureADContentQueryReply:
    """
    Retrieve Microsoft Entra ID Objects from the Microsoft Entra ID Server (formerly, Azure AD).

    Parameters
    ----------
    client : ClientSession [Argument]
    data : AzureADContentRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    AzureADContentQueryReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-azure-ad-content"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return AzureADContentQueryReply(**resp)
