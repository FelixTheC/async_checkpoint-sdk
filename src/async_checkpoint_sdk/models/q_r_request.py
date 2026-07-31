from pydantic import BaseModel, Field


class QRRequest(BaseModel):
    key_type: str = Field(
        alias="key-type",
        description="""The type of the key parameter.<br>Use predefined for these keys: type-in-data-center, name-in-data-center, and ip-address.<br>Use tag to query the Data Center tag's property.""",
    )
    key: str = Field(
        alias="key",
        description="""Defines in which Data Center property to query.<br>For key-type predefined, use these keys: type-in-data-center, name-in-data-center, and ip-address.<br>For key-type tag, use the Data Center tag key to query.<br>Keys are case-insensitive.""",
    )
    values: list[str] = Field(
        alias="values",
        description="""The value(s) of the Data Center property to match the Query Rule.<br>Values are case-insensitive.<br>There is an 'OR' operation between multiple values.<br>For key-type predefined and key 'ip-address', the values must be an IPv4 or IPv6 address.<br>For key-type tag, the values must be the Data Center tag values.""",
    )
