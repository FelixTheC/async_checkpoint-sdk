from aiohttp import ClientSession

from async_checkpoint_sdk.models.secu_remote_dns_reply import SecuRemoteDnsReply
from async_checkpoint_sdk.models.secu_remote_dns_request_edit import SecuRemoteDnsRequestEdit
from config import Config


async def set_securemote_dns_server(
    client: ClientSession, data: SecuRemoteDnsRequestEdit, config: Config, **kwargs
) -> SecuRemoteDnsReply:
    """
    Edit existing SecuRemote DNS server using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SecuRemoteDnsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SecuRemoteDnsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-securemote-dns-server"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SecuRemoteDnsReply(**resp)
