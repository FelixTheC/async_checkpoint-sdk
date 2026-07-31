from pydantic import BaseModel, Field


class CloudDisconnectMgmtRequest(BaseModel):
    force: bool = Field(
        alias="force",
        description="""Disconnect the Management Server from Check Point Infinity Portal, and reset the connection locally, regardless of the result in the Infinity Portal. This flag can be used if the disconnect-cloud-services command failed. Since with this flag this command affects only the local configuration, make sure to disconnect the Management Server in the Infinity Portal as well.""",
    )
