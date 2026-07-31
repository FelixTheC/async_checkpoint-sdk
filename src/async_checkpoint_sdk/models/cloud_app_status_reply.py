from .api_date_reply import ApiDateReply
from .pydantic import BaseModel, Field


class CloudAppStatusReply(BaseModel):
    access_key: str = Field(alias="access-key", description="""N/A""")
    client_id: str = Field(alias="client-id", description="""N/A""")
    cloud_infra_url: str = Field(alias="cloud-infra-url", description="""N/A""")
    display_name: str = Field(alias="display-name", description="""N/A""")
    key_expiration: ApiDateReply = Field(alias="key-expiration", description="""N/A""")
    role: str = Field(alias="role", description="""N/A""")
