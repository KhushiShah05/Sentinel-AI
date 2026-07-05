from google.adk.agents import Agent

report_agent = Agent(
    name="Report_Agent",
    description="Generates the final audit report.",
    instruction="""
Summarize all security findings into one concise audit report.
"""
)