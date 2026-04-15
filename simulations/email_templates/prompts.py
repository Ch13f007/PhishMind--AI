# PhishMind AI — Email Simulation Prompt Templates
# These prompts guide the Claude API to generate realistic,
# role-specific phishing email simulations for awareness training.

PHISHING_EMAIL_PROMPT = """
You are a security awareness trainer generating a SIMULATED phishing email for training purposes only.

Generate a realistic phishing email for:
- Employee Name: {employee_name}
- Job Role: {role}
- Industry: {industry}
- Simulation Theme: {theme}  (e.g. invoice, IT support, HR, delivery, bank)

Return JSON with:
- subject: email subject line
- sender_name: fake sender display name
- sender_email: fake sender email
- body: full email body (HTML)
- red_flags: list of 3-5 red flags the employee should have spotted

Keep it realistic and role-specific. For SECURITY AWARENESS TRAINING only.
"""

# Common themes per industry
INDUSTRY_THEMES = {
    "fintech": ["account suspension", "suspicious transaction", "KYC verification required"],
    "healthcare": ["patient record update", "compliance audit", "system upgrade"],
    "ecommerce": ["delivery failed", "order refund", "supplier invoice"],
    "general": ["IT password reset", "HR policy update", "payroll notification"]
}
