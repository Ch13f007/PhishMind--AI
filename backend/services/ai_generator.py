"""
PhishMind AI — AI Simulation Generator
Uses the Anthropic Claude API to generate personalised phishing simulations
based on employee role and industry context.
"""

import anthropic
import os


client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate_phishing_email(employee_name: str, role: str, industry: str) -> dict:
    """
    Generate a personalised phishing email simulation.
    Returns subject, sender_name, and body.
    """
    prompt = f"""
    You are a security awareness trainer generating a SIMULATED phishing email for training purposes only.
    
    Generate a realistic but clearly fictional phishing email for:
    - Employee Name: {employee_name}
    - Job Role: {role}
    - Industry: {industry}
    
    Return a JSON object with:
    - "subject": email subject line
    - "sender_name": fake sender display name
    - "sender_email": fake sender email address
    - "body": full email body (HTML)
    - "red_flags": list of red flags employees should spot
    
    Make it realistic and role-specific. This is for security awareness training only.
    """

    # TODO: Implement full Claude API call
    # message = client.messages.create(
    #     model="claude-sonnet-4-20250514",
    #     max_tokens=1000,
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # return parse_response(message.content[0].text)

    return {"status": "not yet implemented"}


def generate_smishing_message(employee_name: str, role: str, industry: str) -> dict:
    """
    Generate a personalised smishing (SMS/WhatsApp) simulation.
    Returns message text and red flags.
    """
    # TODO: Implement smishing generation
    return {"status": "not yet implemented"}


def generate_awareness_training(simulation_type: str, red_flags: list) -> str:
    """
    Generate instant, bite-sized awareness training content
    triggered when an employee clicks a simulation link.
    """
    # TODO: Implement awareness training generation
    return "Awareness training content coming soon."
