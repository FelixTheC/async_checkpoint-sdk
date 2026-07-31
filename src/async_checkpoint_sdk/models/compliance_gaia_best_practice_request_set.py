from pydantic import BaseModel, Field


class ComplianceGaiaBestPracticeRequestSet(BaseModel):
    best_practice_id: str = Field(alias="best-practice-id", description="""Best Practice ID.""")
    action_item: str = Field(
        alias="action-item", description="""To comply with Best Practice, do this action item."""
    )
    description: str = Field(
        alias="description", description="""Description of the Best Practice."""
    )
    expected_output_text: str = Field(
        alias="expected-output-text",
        description="""The expected output of the script as plain text.""",
    )
    new_name: str = Field(alias="new-name", description="""New name of the object.""")
    practice_script_path: str = Field(
        alias="practice-script-path",
        description="""The absolute path of the script on the Management Server to run on Gaia Security Gateways during the Compliance scans.""",
    )
    details_level: str = Field(
        alias="details-level",
        description="""The level of detail for some of the fields in the response can vary from showing only the UID value of the object to a fully detailed representation of the object.""",
    )
    ignore_warnings: bool = Field(
        alias="ignore-warnings", description="""Apply changes ignoring warnings."""
    )
    ignore_errors: bool = Field(
        alias="ignore-errors",
        description="""Apply changes ignoring errors. You won't be able to publish such a changes. If ignore-warnings flag was omitted - warnings will also be ignored.""",
    )
