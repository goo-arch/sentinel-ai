def analyze_log(log_data):
    suspicious_events = []

    for entry in log_data:
        if "failed" in entry.lower():
            suspicious_events.append(entry)

    return suspicious_events


if __name__ == "__main__":
    sample_logs = [
        "User login successful",
        "Multiple failed login attempts detected"
    ]

    print(analyze_log(sample_logs))
