from aiohttp import ClientSession

from async_checkpoint_sdk.models.cp_password_requirements_reply import CpPasswordRequirementsReply
from async_checkpoint_sdk.models.cp_password_requirements_request_show import (
    CpPasswordRequirementsRequestShow,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def show_cp_password_requirements(
    client: ClientSession, data: CpPasswordRequirementsRequestShow, config: SDKConfig, **kwargs
) -> CpPasswordRequirementsReply:
    """
    Retrieve existing Check Point password requirements.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CpPasswordRequirementsRequestShow [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CpPasswordRequirementsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/show-cp-password-requirements"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CpPasswordRequirementsReply(**resp)
