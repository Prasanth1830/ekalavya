import streamlit as st
import time

st.header("Logs")
st.write("This page displays real-time logs of agent and crew activities.")

log_container = st.empty()

mock_logs = [
    "[INFO] Crew starting...",
    "[INFO] Agent 'researcher' starting task...",
    "[DEBUG] Searching web for 'AI advancements'",
    "[DEBUG] Found 10 results.",
    "[INFO] Agent 'researcher' completed task.",
    "[INFO] Agent 'reporting_analyst' starting task...",
    "[DEBUG] Analyzing data from researcher.",
    "[WARNING] Data point 'source_url' is missing. Skipping.",
    "[DEBUG] Generating report.",
    "[INFO] Agent 'reporting_analyst' completed task.",
    "[ERROR] Failed to save report to disk: Permission denied.",
    "[INFO] Crew run finished.",
]

log_content = ""
for log_line in mock_logs:
    log_content += log_line + "\n"
    log_container.code(log_content, language="log")
    time.sleep(0.5)

