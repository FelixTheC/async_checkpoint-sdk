from config import Config
from aiohttp import ClientSession
from models.md_permissions_profile_reply import MdPermissionsProfileReply
from models.api_visual_c_p_object_identifier_request_show import (
    ApiVisualCPObjectIdentifierRequestShow,
)


async def show_md_permissions_profile(
    client: ClientSession, data: ApiVisualCPObjectIdentifierRequestShow, config: Config, **kwargs
) -> MdPermissionsProfileReply:
    """
    Retrieve existing Multi-Domain Permissions Profile using object name or uid.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : ApiVisualCPObjectIdentifierRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    MdPermissionsProfileReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-md-permissions-profile"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return MdPermissionsProfileReply(**resp)
