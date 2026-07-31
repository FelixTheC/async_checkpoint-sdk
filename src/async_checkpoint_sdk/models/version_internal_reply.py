from .pydantic import BaseModel, Field


class VersionInternalReply(BaseModel):
    api_jhf_revision: int = Field(alias="api-jhf-revision", description="""N/A""")
    branch: str = Field(alias="branch", description="""N/A""")
    generation_date: str = Field(alias="generation-date", description="""N/A""")
    os_build: str = Field(alias="os-build", description="""N/A""")
    os_edition: str = Field(alias="os-edition", description="""N/A""")
    os_kernel_version: str = Field(alias="os-kernel-version", description="""N/A""")
    product_version: str = Field(alias="product-version", description="""N/A""")
