from pydantic import BaseModel, Field


class ChangeIpsRequest(BaseModel):
    server_name: str = Field(
        alias="server-name",
        description="""The object name of the server that migrates to a new IP address.""",
    )
    new_ipv4_address: str = Field(
        alias="new-ipv4-address",
        description="""The new IPv4 address of the server that migrates to a new IP address.""",
    )
