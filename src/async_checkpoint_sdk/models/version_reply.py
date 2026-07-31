from .pydantic import BaseModel, Field


class VersionReply(BaseModel):
    os_build: str = Field(alias="os-build", description="""N/A""")
    os_edition: str = Field(alias="os-edition", description="""N/A""")
    os_kernel_version: str = Field(alias="os-kernel-version", description="""N/A""")
    product_version: str = Field(alias="product-version", description="""N/A""")
