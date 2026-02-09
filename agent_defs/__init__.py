from agents import Agent
from services.tools import log_experiment, summarize_results, suggest_next_steps

logger_agent = Agent(name="Logger Agent", instructions="Log experiments with log_experiment.", tools=[log_experiment], model="gpt-4o-mini")
analysis_agent = Agent(name="Analysis Agent", instructions="Summarize experiments with summarize_results.", tools=[summarize_results], model="gpt-4o-mini")
followup_agent = Agent(name="Follow-Up Agent", instructions="Suggest next steps with suggest_next_steps.", tools=[suggest_next_steps], model="gpt-4o-mini")

triage_agent = Agent(
    name="Triage Agent",
    instructions="Log experiment -> Logger Agent. Summarize -> Analysis Agent. Next action -> Follow-Up Agent.",
    handoffs=[logger_agent, analysis_agent, followup_agent],
    model="gpt-4o-mini",
)
