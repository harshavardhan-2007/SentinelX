import re
def analyse_email(email_text):
    score=0
    reasons=[]
    suspicious_keyeords=[
        "urgent",
        "verify",
        "bank",
        "password",
        "click",
        "winner",
        "free",
        "bonus",
        "claim",
        "limited time",
        "account suspended",
        "otp"
    ]
    for word in suspicious_keyeords:
        if word.lower() in email_text.lower():
            score+=1
            reasons.append(f"Suspicious keyword detected: {word}")
    url_pattern=r"https?://\\s+"
    if re.search(url_pattern,email_text):
        score+=2
        reasons.append("Contains suspicious Links!")
    if email_text.count("!")>3:
        score+=1
        reasons.append("Too many exclamation marks")
    if email_text.isupper():
        score+=2
        reasons.append("Entire eamil is uppercase!")
    return score,reasons
