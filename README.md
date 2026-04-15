# PhishMind AI

> Adaptive AI-Powered Phishing Awareness for African SMEs

[![Status](https://img.shields.io/badge/status-in%20development-yellow)]()
[![Stack](https://img.shields.io/badge/backend-Python%20%2B%20FastAPI-blue)]()
[![AI](https://img.shields.io/badge/AI-Claude%20API-purple)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

---

## The Problem

Small and medium-sized enterprises (SMEs) across Africa face a growing wave of phishing and smishing (SMS/WhatsApp) attacks — yet have no access to affordable, adaptive security awareness tools.

- Enterprise tools like **KnowBe4** cost thousands of dollars per year
- Free tools like **GoPhish** are static and show no measurable improvement over time
- There is **no solution** designed and priced for the African SME market

---

## The Solution

**PhishMind AI** is an adaptive security awareness platform that uses AI to generate personalised phishing simulations for each employee — based on their role and industry — and tracks their risk level over time.

### Core Features (MVP)
- **AI-generated simulations** — personalised phishing emails and smishing messages per employee role and industry
-  **Risk scoring** — tracks employee behaviour over time with plain-English explanations
- **Instant awareness training** — triggered the moment an employee clicks a simulated phishing link
- **Admin dashboard** — launch campaigns, monitor results, and generate reports
- **Affordable pricing** — designed specifically for African SMEs

---

## Architecture

```
phishmind-ai/
├── backend/                  # Python + FastAPI
│   ├── main.py               # App entry point
│   ├── routes/               # API route handlers
│   │   ├── campaigns.py      # Campaign management
│   │   ├── employees.py      # Employee management
│   │   └── tracking.py       # Click tracking & risk scoring
│   ├── models/               # Database models
│   │   ├── campaign.py
│   │   ├── employee.py
│   │   └── click_event.py
│   ├── services/             # Business logic
│   │   ├── ai_generator.py   # Claude API integration
│   │   ├── email_sender.py   # SendGrid integration
│   │   └── sms_sender.py     # Twilio integration
│   └── database.py           # DB connection (SQLite → PostgreSQL)
│
├── frontend/                 # React + Tailwind CSS
│   ├── src/
│   │   ├── pages/            # Dashboard, Campaigns, Employees, Reports
│   │   ├── components/       # Reusable UI components
│   │   └── api/              # API client
│   └── package.json
│
├── simulations/              # AI prompt templates
│   ├── email_templates/      # Phishing email prompt templates
│   └── sms_templates/        # Smishing prompt templates
│
├── docs/                     # Technical documentation
│   └── PhishMind_AI_Technical_Documentation.docx
│
├── .env.example              # Environment variable template
├── .gitignore
├── requirements.txt          # Python dependencies
└── README.md
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.11 + FastAPI |
| Frontend | React 18 + Tailwind CSS |
| AI / LLM | Anthropic Claude API |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Email Delivery | SendGrid |
| SMS / WhatsApp | Twilio |
| Hosting | Railway / Render |

---

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- Anthropic API key
- SendGrid API key
- Twilio account SID + Auth token

### Backend Setup
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/phishmind-ai.git
cd phishmind-ai

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy and configure environment variables
cp .env.example .env

# Run the backend
cd backend
uvicorn main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---

## Environment Variables

Copy `.env.example` to `.env` and fill in your keys:

```
ANTHROPIC_API_KEY=your_claude_api_key
SENDGRID_API_KEY=your_sendgrid_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
TWILIO_PHONE_NUMBER=your_twilio_number
DATABASE_URL=sqlite:///./phishmind.db
SECRET_KEY=your_secret_key
```

---

## Roadmap

### MVP (Hackathon)
- [x] Project scaffold and documentation
- [ ] FastAPI backend — campaign and employee management
- [ ] Claude API integration — AI simulation generation
- [ ] SendGrid email delivery + click tracking
- [ ] Twilio SMS/WhatsApp smishing delivery
- [ ] React admin dashboard
- [ ] Risk scoring engine
- [ ] Instant awareness training on click

### Post-MVP
- [ ] Multi-language support for broader African markets
- [ ] LMS integration for extended training modules
- [ ] Enterprise API access
- [ ] Mobile app for employee-facing training

---

## Author

Tatenda Chitanda
Built with ❤️ for the Cybersecurity Hackathon.

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.
