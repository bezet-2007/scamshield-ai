import re

def detect_scam(message):
    keywords = [
        "urgent", "otp", "password", "verify account",
        "click link", "prize", "winner", "bank",
        "upi", "refund", "investment"
    ]

    message_lower = message.lower()
    found = [word for word in keywords if word in message_lower]

    if found:
        print("\n⚠️ Suspicious message detected!")
        print("Warning signs:", ", ".join(found))
        print("Safety tip: Do not share OTP, passwords, or financial details.")
    else:
        print("\n✅ No obvious scam indicators detected.")

message = input("Enter a message to check: ")
detect_scam(message)
