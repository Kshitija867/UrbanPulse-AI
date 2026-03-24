from datetime import datetime

def log_decision(data):
    with open("logs/audit_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | {data}\n\n")