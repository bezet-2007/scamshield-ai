from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="SCAMSHIELD AI")


class MessageRequest(BaseModel):
    message: str


scam_keywords = [
    "urgent",
    "otp",
    "password",
    "verify account",
    "click link",
    "prize",
    "winner",
    "bank",
    "upi",
    "refund",
    "investment"
]


@app.get("/")
def home():
    return {"message": "SCAMSHIELD AI is running"}


@app.post("/detect")
def detect_scam(request: MessageRequest):
    message = request.message.lower()

    found = [
        keyword for keyword in scam_keywords
        if keyword in message
    ]

    if found:
        return {
            "result": "Suspicious",
            "warning_signs": found,
            "safety_tip": "Do not share OTP, passwords, or financial details."
        }

    return {
        "result": "No obvious scam indicators",
        "warning_signs": [],
        "safety_tip": "Stay alert before clicking unknown links."
    }
