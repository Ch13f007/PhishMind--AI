"""
PhishMind AI — Mock AI Simulation Generator
Generates realistic phishing simulations without needing a real API key.
We will swap this for the real Claude API after the hackathon demo.
"""

import random


MOCK_EMAIL_SIMULATIONS = {
    "fintech": [
        {
            "subject": "Urgent: Your Sentracore Account Has Been Suspended",
            "sender_name": "Sentracore Security Team",
            "sender_email": "security@sentracore-alert.com",
            "body": """
                <p>Dear {name},</p>
                <p>We have detected suspicious activity on your Sentracore account. 
                Your account has been <strong>temporarily suspended</strong>.</p>
                <p>To restore access, please verify your identity immediately by clicking the link below:</p>
                <p><a href='{tracking_url}'>Verify My Sentracore Account Now</a></p>
                <p>Failure to verify within 24 hours will result in permanent account closure.</p>
                <p>Regards,<br>Sentracore Security Team</p>
            """,
            "red_flags": [
                "Sender email domain is 'sentracore-alert.com' not 'sentracore.com'",
                "Creates urgency with 24 hour deadline",
                "Threatens account closure to pressure action",
                "Generic greeting instead of your full name"
            ]
        },
        {
            "subject": "Action Required: Sentracore KYC Verification Needed",
            "sender_name": "Sentracore Compliance Department",
            "sender_email": "compliance@sentracore-kyc-verify.com",
            "body": """
                <p>Dear {name},</p>
                <p>As part of our regulatory compliance, all Sentracore employees must 
                complete KYC verification by end of day.</p>
                <p>Please click below to submit your details:</p>
                <p><a href='{tracking_url}'>Complete Sentracore KYC Verification</a></p>
                <p>Non-compliance may result in system access revocation.</p>
                <p>Regards,<br>Sentracore Compliance Department</p>
            """,
            "red_flags": [
                "Suspicious domain 'sentracore-kyc-verify.com' not 'sentracore.com'",
                "Unrealistic same-day deadline",
                "Threatens access revocation",
                "No official Sentracore logo or branding"
            ]
        }
    ],
    "healthcare": [
        {
            "subject": "Urgent: Patient Record Update Required",
            "sender_name": "Sentracore IT Support",
            "sender_email": "itsupport@sentracore-records-update.com",
            "body": """
                <p>Dear {name},</p>
                <p>Our system has flagged your patient records portal as requiring 
                an urgent security update.</p>
                <p>Please log in immediately to prevent data loss:</p>
                <p><a href='{tracking_url}'>Update My Records Portal</a></p>
                <p>Sentracore IT Support Team</p>
            """,
            "red_flags": [
                "Domain does not match any official Sentracore domain",
                "Vague threat of data loss",
                "No specific details about what needs updating",
                "Unusual sender for a records update"
            ]
        }
    ],
    "ecommerce": [
        {
            "subject": "Your Sentracore Package Could Not Be Delivered",
            "sender_name": "Sentracore Delivery Team",
            "sender_email": "delivery@sentracore-express-alert.com",
            "body": """
                <p>Dear {name},</p>
                <p>We attempted to deliver your Sentracore order today but were unsuccessful.</p>
                <p>To reschedule your delivery, please confirm your address and 
                pay a small redelivery fee of ₦500:</p>
                <p><a href='{tracking_url}'>Reschedule My Delivery</a></p>
                <p>Sentracore Delivery Team</p>
            """,
            "red_flags": [
                "Domain is 'sentracore-express-alert.com' not 'sentracore.com'",
                "Requests payment via a link",
                "No tracking number provided",
                "No specific order details mentioned"
            ]
        }
    ],
    "general": [
        {
            "subject": "Your Sentracore Password Will Expire in 24 Hours",
            "sender_name": "Sentracore IT Helpdesk",
            "sender_email": "helpdesk@sentracore-it-portal.com",
            "body": """
                <p>Dear {name},</p>
                <p>Your Sentracore account password is due to expire in <strong>24 hours</strong>.</p>
                <p>Please click the link below to reset your password immediately:</p>
                <p><a href='{tracking_url}'>Reset My Sentracore Password Now</a></p>
                <p>Sentracore IT Helpdesk</p>
            """,
            "red_flags": [
                "Domain 'sentracore-it-portal.com' is not an official Sentracore domain",
                "Creates urgency with 24 hour deadline",
                "Real IT teams don't send password resets via external links",
                "No official Sentracore branding or logo"
            ]
        }
    ]
}


MOCK_SMS_SIMULATIONS = {
    "fintech": [
        {
            "message": "SENTRACORE ALERT: Suspicious login detected on your account. Verify now or your account will be locked: {tracking_url}",
            "red_flags": [
                "Unsolicited SMS with a link",
                "Creates urgency with lock threat",
                "Short URL hides real destination"
            ]
        }
    ],
    "general": [
        {
            "message": "Congratulations! You have won a Sentracore ₦50,000 prize. Click to claim: {tracking_url}",
            "red_flags": [
                "Too good to be true prize offer",
                "Unsolicited message from unknown number",
                "Suspicious link to claim prize"
            ]
        }
    ]
}


def generate_phishing_email(employee_name: str, role: str, industry: str) -> dict:
    simulations = MOCK_EMAIL_SIMULATIONS.get(industry, MOCK_EMAIL_SIMULATIONS["general"])
    simulation = random.choice(simulations)
    simulation = simulation.copy()
    simulation["body"] = simulation["body"].replace("{name}", employee_name)
    simulation["body"] = simulation["body"].replace("{industry}", industry)
    return simulation


def generate_smishing_message(employee_name: str, role: str, industry: str) -> dict:
    simulations = MOCK_SMS_SIMULATIONS.get(industry, MOCK_SMS_SIMULATIONS["general"])
    simulation = random.choice(simulations)
    return simulation.copy()


def generate_awareness_training(red_flags: list) -> str:
    flags_html = "".join([f"<li>{flag}</li>" for flag in red_flags])
    return f"""
    <h2>⚠️ You clicked a simulated phishing link!</h2>
    <p>Don't worry — this was a <strong>safe training simulation</strong> by Sentracore.</p>
    <h3>Here's what you should have spotted:</h3>
    <ul>{flags_html}</ul>
    <h3>Remember:</h3>
    <ul>
        <li>Always check the sender's email domain carefully</li>
        <li>Never click links in urgent or threatening emails</li>
        <li>When in doubt, contact your IT team directly</li>
        <li>Legitimate companies never ask for passwords via email</li>
    </ul>
    <p><strong>Stay vigilant! 🛡️</strong></p>
    """