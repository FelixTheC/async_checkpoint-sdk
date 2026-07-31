from pydantic import BaseModel, Field


class ComplianceUserDefinedGaiaOsReply(BaseModel):
    expected_output_base64: str = Field(
        alias="expected-output-base64",
        description="""The expected output of the script in the Base64.""",
    )
    practice_script_base64: str = Field(
        alias="practice-script-base64",
        description="""The script in Base64 to run on Gaia Security Gateways during the Compliance scans.""",
    )
