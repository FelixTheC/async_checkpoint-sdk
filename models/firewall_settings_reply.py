from pydantic import BaseModel, Field


class FirewallSettingsReply(BaseModel):
    auto_calculate_connections_hash_table_size_and_memory_pool: bool = Field(
        alias="auto-calculate-connections-hash-table-size-and-memory-pool",
        description="""N/A""",
    )
    auto_maximum_limit_for_concurrent_connections: bool = Field(
        alias="auto-maximum-limit-for-concurrent-connections", description="""N/A"""
    )
    connections_hash_size: int = Field(
        alias="connections-hash-size", description="""N/A"""
    )
    maximum_limit_for_concurrent_connections: int = Field(
        alias="maximum-limit-for-concurrent-connections", description="""N/A"""
    )
    maximum_memory_pool_size: int = Field(
        alias="maximum-memory-pool-size", description="""N/A"""
    )
    memory_pool_size: int = Field(alias="memory-pool-size", description="""N/A""")
