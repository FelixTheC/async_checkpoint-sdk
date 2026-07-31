from pydantic import BaseModel, Field

from .add import add
from .remove import remove


class AccessLayerRequestEdit(BaseModel):
    applications_and_url_filtering: bool = Field(
        alias="applications-and-url-filtering",
        description="""Whether to enable Applications & URL Filtering blade on the layer.""",
    )
    content_awareness: bool = Field(
        alias="content-awareness",
        description="""Whether to enable Content Awareness blade on the layer.""",
    )
    detect_using_x_forward_for: bool = Field(
        alias="detect-using-x-forward-for",
        description="""Whether to use X-Forward-For HTTP header, which is added by the  proxy server to keep track of the original source IP.""",
    )
    dynamic_layer: bool = Field(
        alias="dynamic-layer",
        description="""Whether this layer is set as a Dynamic layer.""",
    )
    firewall: bool = Field(
        alias="firewall",
        description="""Whether to enable Firewall blade on the layer.""",
    )
    implicit_cleanup_action: str = Field(
        alias="implicit-cleanup-action",
        description="""The default catch-all action for traffic that does not match any explicit or implied rules in the layer.""",
    )
    mobile_access: bool = Field(
        alias="mobile-access",
        description="""Whether to enable Mobile Access blade on the layer.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    shared: bool = Field(alias="shared", description="""Whether this layer is shared.""")
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from .showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    tags: add | remove | str | list[str] = Field(
        alias="tags", description="""Collection of tag identifiers."""
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
