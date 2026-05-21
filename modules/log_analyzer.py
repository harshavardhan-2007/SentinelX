import re

def analyze_logs(log_text):

    failed_logins = {}
    unauthorized_count = 0
    alerts = []

    lines = log_text.splitlines()

    for line in lines:

        line = line.strip()

        # Failed login detection
        if "failed login" in line.lower():

            match = re.search(
                r'(\d+\.\d+\.\d+\.\d+)',
                line
            )

            if match:

                ip = match.group(1)

                failed_logins[ip] = (
                    failed_logins.get(ip, 0) + 1
                )

        # Unauthorized access detection
        if "unauthorized access" in line.lower():

            unauthorized_count += 1

    total_failed = sum(failed_logins.values())

    # Brute force detection
    for ip, count in failed_logins.items():

        if count >= 3:

            alerts.append(
                f"Possible brute force attack from {ip} ({count} attempts)"
            )

    # Unauthorized alerts
    if unauthorized_count > 0:

        alerts.append(
            "Unauthorized access detected!"
        )

    return {
        "total_failed": total_failed,
        "unauthorized_count": unauthorized_count,
        "alerts": alerts
    }