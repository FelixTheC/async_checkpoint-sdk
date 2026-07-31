from .pydantic import BaseModel, Field


class IdentityAwarenessGlobalPropertiesReply(BaseModel):
    cache_mode: bool = Field(
        alias="cache-mode",
        description="""True: In case of connectivity loss from .the Policy-Decision-Point (PDP), extend Identity cache up-to cache-mode-duration.<br>False: Identity Cache Mode is disabled, in case of connectivity loss from .the Policy-Decision-Point, existing Identities will be lost immediately.""",
    )
    cache_mode_duration: int = Field(
        alias="cache-mode-duration",
        description="""Time limit for keeping Identities in the cache.""",
    )
