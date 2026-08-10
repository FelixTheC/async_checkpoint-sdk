from aiohttp import ClientSession

from async_checkpoint_sdk.models.secu_remote_dns_reply import SecuRemoteDnsReply
from async_checkpoint_sdk.models.secu_remote_dns_request_edit import SecuRemoteDnsRequestEdit
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def clone_securemote_dns_server(
    client: ClientSession, data: SecuRemoteDnsRequestEdit, config: SDKConfig, **kwargs
) -> SecuRemoteDnsReply:
    """
    Clone existing SecuRemote DNS server.

    Parameters
    ----------
    client : ClientSession
    data : SecuRemoteDnsRequestEdit
    config : SDKConfig
    kwargs : Any
        Keyword arguments

    Returns
    -------
    SecuRemoteDnsReply

    """
    url = f"https://{config.server}:{config.port}/web_api/clone-securemote-dns-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecuRemoteDnsReply(**resp)
