from pydantic import BaseModel, Field


class ViewCentralLicensesReply(BaseModel):
    available_quota: str = Field(
        alias="available-quota",
        description="""The difference between the pool's total quota and the total cores quantity of the pool's subscribed Gateways.""",
    )
    cks: list[str] = Field(
        alias="cks",
        description="""List of the licenses CKs (Certificate Keys) that belong to this license pool.""",
    )
    is_default: bool = Field(
        alias="is-default",
        description="""The default pool is the license pool that distributes its licenses to the CloudGuard Gateways unless configured otherwise.""",
    )
    pool: str = Field(
        alias="pool",
        description="""A group of CloudGuard Central Licenses with the same valid contract blades.""",
    )
    total_quota: str = Field(
        alias="total-quota",
        description="""A license pool total quota is the total quantity of all the virtual cores provided by all the Central Licenses in this pool.""",
    )
    subscribed_gateways: list[dict] = Field(
        alias="subscribed-gateways",
        description="""List of the subscribed CloudGuard Gateways of this license pool.""",
    )
