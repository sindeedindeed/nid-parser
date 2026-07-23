from pydantic import BaseModel, Field
from typing import Optional

class NIDResponse(BaseModel):
    name: Optional[str] = Field(None, description="Full Name in English")
    father_name: Optional[str] = Field(None, alias="fatherName")
    mother_name: Optional[str] = Field(None, alias="motherName")
    date_of_birth: Optional[str] = Field(None, alias="dateOfBirth", description="YYYY-MM-DD")
    nid_number: Optional[str] = Field(None, alias="nidNumber")
    address: Optional[str] = Field(None, alias="Address")
    blood_group: Optional[str] = Field(None, alias="bloodGroup")
    issue_date: Optional[str] = Field(None, alias="issueDate", description="YYYY-MM-DD")
    
    class Config:
        populate_by_name = True