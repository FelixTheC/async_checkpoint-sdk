from pydantic import BaseModel, Field


class QRRequest(BaseModel):
    values: list[str] = Field(
        alias="values",
        description="""The value(s) of the Data Center property to match the Query Rule.<br>Values are case-insensitive.<br>There is an 'OR' operation between multiple values.<br>For key-type predefined and key 'ip-address', the values must be an IPv4 or IPv6 address.<br>For key-type tag, the values must be the Data Center tag values.""",
    )
