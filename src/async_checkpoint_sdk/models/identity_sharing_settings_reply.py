from .identity_cache_mode_duration_settings_reply import (
    IdentityCacheModeDurationSettingsReply,
)
from .identity_cache_mode_settings_reply import IdentityCacheModeSettingsReply
from .pydantic import BaseModel, Field


class IdentitySharingSettingsReply(BaseModel):
    share_with_other_gateways: bool = Field(
        alias="share-with-other-gateways",
        description="""Enable identity sharing with other gateways.""",
    )
    receive_from_infinity_identity: bool = Field(
        alias="receive-from-infinity-identity",
        description="""Enable receiving identities from .Infinity Identity.""",
    )
    receive_from_other_gateways: bool = Field(
        alias="receive-from-other-gateways",
        description="""Enable receiving identity from .other gateways.""",
    )
    receive_from: list[str] = Field(
        alias="receive-from", description="""Gateway(s) to receive identity from."""
    )
    cache_mode: IdentityCacheModeSettingsReply = Field(
        alias="cache-mode",
        description="""True: In case of connectivity loss from .the Policy-Decision-Point (PDP), extend Identity cache up-to cache-mode-duration.<br>False: Identity Cache Mode is disabled, in case of connectivity loss from .the Policy-Decision-Point, existing Identities will be lost immediately.""",
    )
    cache_mode_duration: IdentityCacheModeDurationSettingsReply = Field(
        alias="cache-mode-duration",
        description="""Time limit for keeping Identities in the cache.""",
    )
    scaled_sharing: bool = Field(alias="scaled-sharing", description="""Enable Scaled Sharing.""")
