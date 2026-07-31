from aiohttp import ClientSession

from async_checkpoint_sdk.models.subordinate_ca_reply import SubordinateCaReply
from async_checkpoint_sdk.models.subordinate_ca_request_edit import SubordinateCaRequestEdit
from config import Config


async def set_subordinate_ca(
    client: ClientSession, data: SubordinateCaRequestEdit, config: Config, **kwargs
) -> SubordinateCaReply:
    """
    Edit existing Subordinate CA server using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : SubordinateCaRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    SubordinateCaReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-subordinate-ca"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return SubordinateCaReply(**resp)
