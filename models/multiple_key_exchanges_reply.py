from api_domain_identifier import ApiDomainIdentifier
from available_actions_reply import AvailableActionsReply
from meta_info_for_top_level_reply import MetaInfoForTopLevelReply
from pydantic import BaseModel, Field


class MultipleKeyExchangesReply(BaseModel):
    name: str = Field(
        alias="name", description="""Object name. Must be unique in the domain."""
    )
    uid: str = Field(alias="uid", description="""Object unique identifier.""")
    type: str = Field(alias="type", description="""Object type.""")
    key_exchange_methods: list[str] = Field(
        alias="key-exchange-methods",
        description="""Key-Exchange methods to use. Can contain only Diffie-Hellman groups.""",
    )
    additional_key_exchange_1_methods: list[str] = Field(
        alias="additional-key-exchange-1-methods",
        description="""Additional Key-Exchange 1 methods to use.""",
    )
    additional_key_exchange_2_methods: list[str] = Field(
        alias="additional-key-exchange-2-methods",
        description="""Additional Key-Exchange 2 methods to use.""",
    )
    additional_key_exchange_3_methods: list[str] = Field(
        alias="additional-key-exchange-3-methods",
        description="""Additional Key-Exchange 3 methods to use.""",
    )
    additional_key_exchange_4_methods: list[str] = Field(
        alias="additional-key-exchange-4-methods",
        description="""Additional Key-Exchange 4 methods to use.""",
    )
    additional_key_exchange_5_methods: list[str] = Field(
        alias="additional-key-exchange-5-methods",
        description="""Additional Key-Exchange 5 methods to use.""",
    )
    additional_key_exchange_6_methods: list[str] = Field(
        alias="additional-key-exchange-6-methods",
        description="""Additional Key-Exchange 6 methods to use.""",
    )
    additional_key_exchange_7_methods: list[str] = Field(
        alias="additional-key-exchange-7-methods",
        description="""Additional Key-Exchange 7 methods to use.""",
    )
    color: str = Field(
        alias="color",
        description="""Color of the object. Should be one of existing colors.""",
    )
    comments: str = Field(alias="comments", description="""Comments string.""")
    domain: ApiDomainIdentifier = Field(
        alias="domain",
        description="""Information about the domain that holds the Object.""",
    )
    icon: str = Field(alias="icon", description="""Object icon.""")
    meta_info: MetaInfoForTopLevelReply = Field(
        alias="meta-info", description="""Object metadata."""
    )
    read_only: bool = Field(
        alias="read-only", description="""Indicates whether the object is read-only."""
    )
    tags: list[dict] = Field(
        alias="tags",
        description="""Collection of tag objects identified by the name or UID. Level of details in the output corresponds to the number of details for search. This table shows the level of details in the Standard level.""",
    )
    available_actions: AvailableActionsReply = Field(
        alias="available-actions",
        description="""Actions that are available on the object.""",
    )
