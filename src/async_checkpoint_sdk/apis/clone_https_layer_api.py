from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_task_reply import ApiTaskReply
from async_checkpoint_sdk.models.clone_https_layer_request import CloneHttpsLayerRequest
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_https_layer(
    client: ClientSession, data: CloneHttpsLayerRequest, config: SDKConfig, **kwargs
) -> ApiTaskReply:
    """
    Clone https layer using layer name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CloneHttpsLayerRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiTaskReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-https-layer"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiTaskReply(**resp)
