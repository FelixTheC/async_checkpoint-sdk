from aiohttp import ClientSession

from async_checkpoint_sdk.models.secur_id_reply import SecurIdReply
from async_checkpoint_sdk.models.secur_id_request_new import SecurIdRequestNew
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def add_securid_server(
    client: ClientSession, data: SecurIdRequestNew, config: SDKConfig, **kwargs
) -> SecurIdReply:
    """
    Create new SecurID server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecurIdRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecurIdReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-securid-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurIdReply(**resp)
