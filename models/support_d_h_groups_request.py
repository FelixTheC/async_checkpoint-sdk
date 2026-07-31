from pydantic import BaseModel, Field


class SupportDHGroupsRequest(BaseModel):
    group1: bool = Field(
        alias="group1",
        description="""Select whether Diffie-Hellman Group 1 (768 bit) will be supported with remote hosts.""",
    )
    group14: bool = Field(
        alias="group14",
        description="""Select whether Diffie-Hellman Group 14 (2048 bit) will be supported with remote hosts.""",
    )
    group15: bool = Field(
        alias="group15",
        description="""Select whether Diffie-Hellman Group 15 (3072 bit) will be supported with remote hosts.""",
    )
    group16: bool = Field(
        alias="group16",
        description="""Select whether Diffie-Hellman Group 16 (4096 bit) will be supported with remote hosts.""",
    )
    group17: bool = Field(
        alias="group17",
        description="""Select whether Diffie-Hellman Group 17 (6144 bit) will be supported with remote hosts.""",
    )
    group18: bool = Field(
        alias="group18",
        description="""Select whether Diffie-Hellman Group 18 (8192 bit) will be supported with remote hosts.""",
    )
    group19: bool = Field(
        alias="group19",
        description="""Select whether Diffie-Hellman Group 19 (256-bit ECP) will be supported with remote hosts.""",
    )
    group2: bool = Field(
        alias="group2",
        description="""Select whether Diffie-Hellman Group 2 (1024 bit) will be supported with remote hosts.""",
    )
    group20: bool = Field(
        alias="group20",
        description="""Select whether Diffie-Hellman Group 20 (384-bit ECP) will be supported with remote hosts.""",
    )
    group21: bool = Field(
        alias="group21",
        description="""Select whether Diffie-Hellman Group 21 (521-bit ECP) will be supported with remote hosts.""",
    )
    group5: bool = Field(
        alias="group5",
        description="""Select whether Diffie-Hellman Group 5 (1536 bit) will be supported with remote hosts.""",
    )
