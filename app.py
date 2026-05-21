from modules.phishing_detector import check_url
from modules.email_scanner import analyse_email
from modules.log_analyzer import analyze_logs
from modules.malware_analyzer import analyze_file,calculate_entropy
import streamlit as st

st.set_page_config(
    page_title="SentinelX",
    layout="wide"
)

st.title("SENTINELX")
st.subheader("AI Powered Cyber Defence Platform")

st.sidebar.title("Modules")

module = st.sidebar.selectbox(
    "Choose Module",
    [
        "Home",
        "Phishing URL Detector",
        "Email Scam Analyzer",
        "Log Analyzer",
        "Malware Analyzer"
    ]
)

if module == "Home":

    st.write("Welcome to SENTINELX!")

elif module == "Phishing URL Detector":

    st.header(" Phishing URL Detector")

    url = st.text_input("Enter URL")

    if st.button("Analyze URL"):

        score, reasons = check_url(url)

        st.subheader(f"Risk Score: {score}")

        if score == -1:
            st.error("Invalid URL")

        elif score >= 5:
            st.error("High Risk Phishing URL")

        elif score >= 3:
            st.warning("Suspicious URL")

        else:
            st.success("Looks Safe")

        st.write("### Reasons")

        for reason in reasons:
            st.write(f"- {reason}")
elif module=="Email Scam Analyzer":
    st.header("Email Scan Analyser!")
    email_text=st.text_area("PASTE YOUR SUSPECTED EMAIL")
    if st.button("Analyze Email"):
        score,reasons=analyse_email(email_text)
        st.subheader(f"Risk Score: {score}")
        if score>=5:
            st.error("High risk scam email !")
        elif score>=3:
            st.warning("Suspicious Email")
        else:
            st.success("Lools Safe! ")
        st.write("### Reasons!")
        for reason in reasons:
            st.write(f"- {reasons}")
elif module=="Log Analyzer":
    st.header("Security Log anlyzer!")
    log_text=st.text_area("Paste Log Data! ")
    if st.button("Analyze log"):
        result=analyze_logs(log_text)
        st.subheader("Analysis Report !")
        st.write(f"Failed Login Attempts: {result['total_failed']}")
        st.write(f"Unauthorized Access Attempts: {result['unauthorized_count']}")
        st.write("### Alerts!")
        if result["alerts"]:
            for alert in result["alerts"]:
                st.error(alert)
        else:
            st.success("No major threats detected!")
elif module=="Malware Analyzer":
    st.header("Malware Analyzer!")
    upload_file=st.file_uploader('Upload a file')
    if upload_file is not None:
        result=analyze_file(upload_file)
        st.subheader("Analysis Report")
        st.write(f"File size: {result['file_size']} bytes")
        st.write(f"Threat Score: {result['score']}")
        st.write(f"Entropy: {result['entropy']}")
        if result['score']>=5:
            st.error("High Risk Malware Detedcted")
        elif result['score']>=3:
            st.warning("Suspicious file !")
        else:
            st.success("Looks Safe! ")
        st.write("### Reasons")
        for reason in result["reasons"]:
                st.write(f"- {reason}")
