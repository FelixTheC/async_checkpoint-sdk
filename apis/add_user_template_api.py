from aiohttp import ClientSession

from config import Config
from models.user_template_reply import UserTemplateReply
from models.user_template_request_new import UserTemplateRequestNew


async def add_user_template(
    client: ClientSession, data: UserTemplateRequestNew, config: Config, **kwargs
) -> UserTemplateReply:
    """
    Create new object.
    
    Parameters
    ----------
    client : ClientSession [Argument]
    data : UserTemplateRequestNew [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    UserTemplateReply
    """
    url = f"https://{config.server}:{config.port}/web_api/add-user-template"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return UserTemplateReply(**resp)
