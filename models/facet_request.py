from pydantic import BaseModel, Field


class FacetRequest(BaseModel):
    field_name: str = Field(alias="field-name", description="""N/A""")
    sort_by: str = Field(alias="sort-by", description="""N/A""")
    sort_order: str = Field(alias="sort-order", description="""N/A""")
    tokenized_search: bool = Field(alias="tokenized-search", description="""N/A""")
