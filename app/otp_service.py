import os
import random
from app.redis_client import redis_client

OTP_EXPIRY_SECONDS = int(os.getenv("OTP_EXPIRY_SECONDS", 120))


def generate_otp() -> str:
    return str(random.randint(100000, 999999))


def send_otp_to_user(mobile_number: str) -> dict:
    otp = generate_otp()

    redis_key = f"otp:{mobile_number}"

    redis_client.setex(
        redis_key,
        OTP_EXPIRY_SECONDS,
        otp
    )

    # In real project, send OTP using SMS provider
    return {
        "message": "OTP sent successfully",
        "mobile_number": mobile_number,
        "otp_for_testing": otp,
        "expires_in_seconds": OTP_EXPIRY_SECONDS
    }


def verify_user_otp(mobile_number: str, otp: str) -> dict:
    redis_key = f"otp:{mobile_number}"

    stored_otp = redis_client.get(redis_key)

    if not stored_otp:
        return {
            "success": False,
            "message": "OTP expired or not found"
        }

    if stored_otp != otp:
        return {
            "success": False,
            "message": "Invalid OTP"
        }

    redis_client.delete(redis_key)

    return {
        "success": True,
        "message": "OTP verified successfully"
    }