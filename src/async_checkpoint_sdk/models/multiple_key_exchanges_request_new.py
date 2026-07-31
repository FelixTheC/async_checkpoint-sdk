from pydantic import BaseModel, Field


class MultipleKeyExchangesRequestNew(BaseModel):
    name: str = Field(alias="name", description="""Object name. Must be unique in the domain.""")
    key_exchange_methods: str | list[str] = Field(
        alias="key-exchange-methods",
        description="""Key-Exchange methods to use. Can contain only Diffie-Hellman groups.""",
    )
    additional_key_exchange_1_methods: str | list[str] = Field(
        alias="additional-key-exchange-1-methods",
        description="""Additional Key-Exchange 1 methods to use.""",
    )
    additional_key_exchange_2_methods: str | list[str] = Field(
        alias="additional-key-exchange-2-methods",
        description="""Additional Key-Exchange 2 methods to use.""",
    )
    additional_key_exchange_3_methods: str | list[str] = Field(
        alias="additional-key-exchange-3-methods",
        description="""Additional Key-Exchange 3 methods to use.""",
    )
    additional_key_exchange_4_methods: str | list[str] = Field(
        alias="additional-key-exchange-4-methods",
        description="""Additional Key-Exchange 4 methods to use.""",
    )
    additional_key_exchange_5_methods: str | list[str] = Field(
        alias="additional-key-exchange-5-methods",
        description="""Additional Key-Exchange 5 methods to use.""",
    )
    additional_key_exchange_6_methods: str | list[str] = Field(
        alias="additional-key-exchange-6-methods",
        description="""Additional Key-Exchange 6 methods to use.""",
    )
    additional_key_exchange_7_methods: str | list[str] = Field(
        alias="additional-key-exchange-7-methods",
        description="""Additional Key-Exchange 7 methods to use.""",
    )
    color: str = Field(
        alias="color", description="""Color of the object. Should be one of existing colors."""
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    domains_to_process: list[str] = Field(
        alias="domains-to-process",
        description="""Indicates which domains to process the commands on. It cannot be used with the details-level full, must be run from the System Domain only and with ignore-warnings true. Valid values are: CURRENT_DOMAIN, ALL_DOMAINS_ON_THIS_SERVER.""",
    )
    tags: str | list[str] = Field(alias="tags", description="""Collection of tag identifiers.""")
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
