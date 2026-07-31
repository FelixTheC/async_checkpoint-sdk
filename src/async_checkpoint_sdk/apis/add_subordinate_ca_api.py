from aiohttp import ClientSession

from async_checkpoint_sdk.models.subordinate_ca_reply import SubordinateCaReply
from async_checkpoint_sdk.models.subordinate_ca_request_new import SubordinateCaRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_subordinate_ca(
    client: ClientSession, data: SubordinateCaRequestNew, config: SDKConfig, **kwargs
) -> SubordinateCaReply:
    """
    Create new Subordinate CA server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SubordinateCaRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SubordinateCaReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-subordinate-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SubordinateCaReply(**resp)
