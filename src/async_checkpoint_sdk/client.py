from types import TracebackType

import aiohttp

from async_checkpoint_sdk import SDKConfig
from async_checkpoint_sdk.apis.login_api import login as login_api
from async_checkpoint_sdk.apis.logout_api import logout as logout_api
from async_checkpoint_sdk.models.web_api_login_reply import WebApiLoginReply
from async_checkpoint_sdk.models.web_api_login_request import WebApiLoginRequest
from async_checkpoint_sdk.models.web_api_logout_request import WebApiLogoutRequest


class CkpLogin:
    domain: str
    data: WebApiLoginReply

    def __init__(self, domain: str, data: WebApiLoginReply):
        """
        Parameters
        ----------
        domain : str
        data : WebApiLoginReply

        """
        self.domain = domain
        self.data = data


class SDKClient:
    session: aiohttp.ClientSession
    domain: str
    auto_logout: bool
    ckp_sessions: list[CkpLogin] = []
    config: SDKConfig = SDKConfig(server="", port=443, username="")

    def __init__(self, domain: str, config: SDKConfig | None = None, auto_logout: bool = False):
        """
        Parameters
        ----------
        domain : str
        config : SDKConfig | None, optional
            default: None
        auto_logout : bool, optional
            default: False

        """
        self.domain = domain
        self.auto_logout = auto_logout
        if config is not None:
            self.config = config

    async def get_sid_from_sessions(self) -> str | None:
        """
        Returns
        -------
        str | None

        """
        for session in self.ckp_sessions:
            if session.domain == self.domain:
                return session.data.sid
        return None

    async def login_to_domain(self) -> str:
        """
        Returns the session ID of the login to the domain.
        
        Returns
        -------
        str

        """
        data = {"user": self.config.username, "domain": self.domain}
        if self.config.password != "" and self.config.api_key == "":
            data["password"] = self.config.password
        elif self.config.api_key != "" and self.config.password == "":
            data["api_key"] = self.config.api_key

        async with aiohttp.ClientSession(headers={"Content-Type": "application/json"}) as client_session:
            res = await login_api(client_session, WebApiLoginRequest(**data), self.config)
        self.ckp_sessions.append(CkpLogin(self.domain, res))
        return res.sid

    async def __aenter__(self):
        domain_sid = await self.get_sid_from_sessions()
        if domain_sid is None:
            domain_sid = await self.login_to_domain()

        self.session = aiohttp.ClientSession(headers={"Content-Type": "application/json", "X-chkp-sid": domain_sid})
        return self.session

    async def __aexit__(self, exc_type: type[BaseException] | None, exc_val: BaseException | None, exc_tb: TracebackType | None):
        """
        Parameters
        ----------
        exc_type : type[BaseException] | None
        exc_val : BaseException | None
        exc_tb : TracebackType | None

        """
        if self.auto_logout:
            await logout_api(self.session, self.config)
        await self.session.close()


if __name__ == "__main__":
    pass
