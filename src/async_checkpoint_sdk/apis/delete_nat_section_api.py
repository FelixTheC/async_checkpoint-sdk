from aiohttp import ClientSession

from async_checkpoint_sdk.models.api_ok_reply import ApiOkReply
from async_checkpoint_sdk.models.nat_section_identifier_request import NatSectionIdentifierRequest
from config import Config


async def delete_nat_section(
    client: ClientSession, data: NatSectionIdentifierRequest, config: Config, **kwargs
) -> ApiOkReply:
    """
    Delete existing object using object name or uid.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : NatSectionIdentifierRequest [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    ApiOkReply
    """
    url = f"https://{config.server}:{config.port}/web_api/delete-nat-section"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return ApiOkReply(**resp)
