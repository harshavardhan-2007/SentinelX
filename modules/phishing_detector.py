import re
import validators

def check_url(url):

    score = 0
    reasons = []

    if not validators.url(url): 
        return -1, ["Invalid URL"]

    if not url.startswith("https://"):
        reasons.append("No HTTPS detected")
        score += 2

    if len(url) > 50:
        reasons.append("URL is too long")
        score += 1

    if "@" in url:
        reasons.append("@ Symbol detected")
        score += 2

    ip_pattern = r"(\\d{1,3}\\.){3}\\d{1,3}"

    if re.search(ip_pattern, url):
        reasons.append("IP address detected in URL")
        score += 3

    keywords = [
        "login",
        "verify",
        "bank",
        "secure",
        "update",
        "free",
        "bonus"
    ]

    for word in keywords:
        if word in url.lower():
            reasons.append(f"Suspicious keyword: {word}")
            score += 1

    return score, reasons