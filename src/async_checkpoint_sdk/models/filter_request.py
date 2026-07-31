from .pydantic import BaseModel, Field


class FilterRequest(BaseModel):
    and_operator_for_query: bool = Field(alias="and-operator-for-query", description="""N/A""")
    field_name: str = Field(alias="field-name", description="""N/A""")
    from_facet: bool = Field(alias="from-facet", description="""N/A""")
    internal_filter: bool = Field(alias="internal-filter", description="""N/A""")
    negate: bool = Field(alias="negate", description="""N/A""")
    primary_filter: bool = Field(alias="primary-filter", description="""N/A""")
    tokenized_search: bool = Field(alias="tokenized-search", description="""N/A""")
    tree_view_relevance: bool = Field(alias="tree-view-relevance", description="""N/A""")
    values: list[str] = Field(alias="values", description="""N/A""")
