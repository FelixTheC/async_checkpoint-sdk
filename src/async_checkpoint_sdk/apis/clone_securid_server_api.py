from aiohttp import ClientSession

from async_checkpoint_sdk.models.secur_id_reply import SecurIdReply
from async_checkpoint_sdk.models.secur_id_request_edit import SecurIdRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_securid_server(
    client: ClientSession, data: SecurIdRequestEdit, config: SDKConfig, **kwargs
) -> SecurIdReply:
    """
    Clone existing SecurID server.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecurIdRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecurIdReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-securid-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecurIdReply(**resp)
