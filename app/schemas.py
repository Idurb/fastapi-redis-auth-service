from pydantic import BaseModel, Field


class SendOTPRequest(BaseModel):
    mobile_number: str = Field(..., example="9876543210")


class VerifyOTPRequest(BaseModel):
    mobile_number: str = Field(..., example="9876543210")
    otp: str = Field(..., example="123456")