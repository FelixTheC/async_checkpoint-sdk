from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class RootSectionReply(BaseModel):
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    children: list[dict] = Field(
        alias="children", description="""Layer children. Children can be of type section or rule."""
    )
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
