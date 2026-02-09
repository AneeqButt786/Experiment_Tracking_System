from typing import Optional
from agents import function_tool

EXPERIMENT_LOG = []

@function_tool
def log_experiment(experiment_name: str, date: str, outcome: str, notes: str) -> str:
    result = {"experiment_name": experiment_name, "date": date, "outcome": outcome, "notes": notes}
    EXPERIMENT_LOG.append(result)
    return f"Logged experiment: {experiment_name}"

@function_tool
def summarize_results(field: Optional[str] = "") -> str:
    if not EXPERIMENT_LOG:
        return "No experiments have been logged yet."
    summary = "Experiment Summary:\n"
    for log in EXPERIMENT_LOG:
        summary += f"- {log['experiment_name']} ({log['date']}): Outcome = {log['outcome']}, Notes: {log['notes']}\n"
    return summary

@function_tool
def suggest_next_steps(field: Optional[str] = "") -> str:
    if not EXPERIMENT_LOG:
        return "No data available."
    last_outcome = EXPERIMENT_LOG[-1]['outcome']
    if "failed" in last_outcome.lower():
        return "Last experiment failed. Suggest replicating with adjusted parameters."
    return "Last experiment succeeded. Suggest scaling to a larger test group."
