# 🛡️ SCAMSHIELD AI

> Detect. Understand. Stay Safe.

SCAMSHIELD AI is an AI-powered scam detection system designed to identify suspicious messages and help users recognize common scam warning signs.

It analyzes message content, detects suspicious indicators, calculates a risk score, classifies the risk level, and provides a safety recommendation.

## 🚀 Features

- Suspicious message detection
- Scam indicator identification
- Automatic risk score
- LOW / MEDIUM / HIGH risk classification
- Safety recommendations
- FastAPI REST API
- Interactive Swagger API documentation
- Planned Indian language support

## 🧠 How It Works

User Message
↓
Message Analysis
↓
Scam Indicator Detection
↓
Risk Score Calculation
↓
Risk Classification
↓
Safety Recommendation
## 📁 Project Structure

scamshield-ai/
│
├── backend/
│   ├── main.py
│   └── scam_detector.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE

## 🛠️ Technology Stack

- Python
- FastAPI
- Pydantic
- Git
- GitHub

## ⚡ API

### POST `/detect`

Analyzes a message and returns its scam risk.

### Request

```json
{
  "message": "URGENT! You won a prize. Verify your bank account and share your OTP."
}
### Response

```json
{
  "result": "Suspicious",
  "risk_level": "HIGH",
  "risk_score": 60,
  "warning_signs": [
    "urgent",
    "otp",
    "prize",
    "bank"
  ],
  "safety_tip": "Do not share OTP, passwords, or financial details."
}
## 📊 Risk Levels

| Score | Risk Level |
|---|---|
| 0–29 | LOW |
| 30–59 | MEDIUM |
| 60–100 | HIGH |
## ▶️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/bezet-2007/scamshield-ai.git
cd scamshield-ai
```
### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Start the API
```bash
uvicorn backend.main:app --reload
```
### 5. Open Swagger
http://127.0.0.1:8000/docs
## 🔮 Future Improvements

- Machine-learning based scam classification
- Suspicious URL analysis
- WhatsApp and SMS scam detection
- Email scam detection
- Indian language support
- Anonymous scam trend tracking
- Web-based interface
- Real-time scam alerts
## 🎯 Why SCAMSHIELD AI?

Online scams can appear convincing and often create urgency or fear.

SCAMSHIELD AI aims to provide users with an additional layer of awareness before they click links, share sensitive information, or make financial decisions.
## 👩‍💻 Developer

**Twilla Bezet Ezhil**

Computer Science Engineering Student  
**St. Joseph's College of Engineering**

### Interests

`Artificial Intelligence` • `Software Development` • `Cybersecurity` • `Innovation`
## 🌱 Project Vision

**Learn → Build → Protect**

SCAMSHIELD AI is being developed as a student project with the goal of exploring how technology can help people recognize potentially harmful digital content.

⭐ If you find this project interesting, consider giving it a star!