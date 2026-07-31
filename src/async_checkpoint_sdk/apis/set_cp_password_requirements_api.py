from aiohttp import ClientSession

from async_checkpoint_sdk.models.cp_password_requirements_reply import CpPasswordRequirementsReply
from async_checkpoint_sdk.models.cp_password_requirements_request_edit import (
    CpPasswordRequirementsRequestEdit,
)
from src.async_checkpoint_sdk.sdk_config import SDKConfig


async def set_cp_password_requirements(
    client: ClientSession, data: CpPasswordRequirementsRequestEdit, config: SDKConfig, **kwargs
) -> CpPasswordRequirementsReply:
    """
    Set Check Point password requirements.

    Parameters
    ----------
    client : ClientSession [Argument]
    data : CpPasswordRequirementsRequestEdit [Argument]
    config : Config [Argument]
    kwargs : [Keyword arguments]

    Returns
    -------
    CpPasswordRequirementsReply
    """
    url = f"https://{config.server}:{config.port}/web_api/set-cp-password-requirements"
    data_obj = {"body": data}
    if client.headers["Content-Type"] == "application/json":
        data_obj = {"json": data}
    async with client.post(url, **data_obj, raise_for_status=True, ssl=False) as response:
        resp = await response.json()
    return CpPasswordRequirementsReply(**resp)
