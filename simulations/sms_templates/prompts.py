# PhishMind AI — SMS/WhatsApp Smishing Prompt Templates

SMISHING_PROMPT = """
You are a security awareness trainer generating a SIMULATED smishing (SMS phishing) message
for employee awareness training. This is for training purposes only.

Generate a realistic smishing SMS for:
- Employee Name: {employee_name}
- Job Role: {role}
- Industry: {industry}
- Theme: {theme}  (e.g. bank alert, package delivery, prize winner, IT alert)

Return JSON with:
- message: the SMS text (max 160 characters)
- fake_link_text: the link text shown in the message
- red_flags: list of 2-3 red flags the employee should have spotted

Keep it realistic. For SECURITY AWARENESS TRAINING only.
"""

SMISHING_THEMES = {
    "fintech": ["account locked", "transfer alert", "card declined"],
    "healthcare": ["appointment reminder", "prescription ready"],
    "ecommerce": ["delivery update", "refund processed"],
    "general": ["prize winner", "IT alert", "verify your account"]
}
