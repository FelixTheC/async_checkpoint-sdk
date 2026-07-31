from config import Config
from aiohttp import ClientSession
from models.user_template_reply import UserTemplateReply
from models.user_template_request_edit import UserTemplateRequestEdit


async def clone_user_template(
    client: ClientSession, data: UserTemplateRequestEdit, config: Config, **kwargs
) -> UserTemplateReply:
    """
    Clone existing object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserTemplateRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserTemplateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/clone-user-template"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserTemplateReply(**resp)
