from fastapi import FastAPI
from app.schemas import SendOTPRequest, VerifyOTPRequest
from app.otp_service import send_otp_to_user, verify_user_otp

app = FastAPI(
    title="Redis OTP Verification API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Redis OTP Verification API is running"
    }


@app.post("/send-otp")
def send_otp(request: SendOTPRequest):
    return send_otp_to_user(request.mobile_number)


@app.post("/verify-otp")
def verify_otp(request: VerifyOTPRequest):
    return verify_user_otp(
        request.mobile_number,
        request.otp
    )