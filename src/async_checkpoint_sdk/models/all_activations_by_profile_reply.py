from activation_reply import ActivationReply
from pydantic import BaseModel, Field


class AllActivationsByProfileReply(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    default: ActivationReply = Field(alias="default", description="""Default settings.""")
    final: ActivationReply = Field(alias="final", description="""Final settings.""")
    override: ActivationReply = Field(alias="override", description="""Settings overrides.""")
