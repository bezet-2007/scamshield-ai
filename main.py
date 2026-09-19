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

    score = min(len(found) * 15, 100)

    if score >= 60:
        risk_level = "HIGH"
    elif score >= 30:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "result": "Suspicious" if found else "No obvious scam indicators",
        "risk_level": risk_level,
        "risk_score": score,
        "warning_signs": found,
        "safety_tip": (
            "Do not share OTP, passwords, or financial details."
            if found
            else "Stay alert before clicking unknown links."
        )
    }