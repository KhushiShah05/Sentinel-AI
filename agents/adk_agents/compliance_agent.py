from google.adk.agents import Agent

compliance_agent = Agent(
    name="Compliance_Agent",
    description="Checks AI compliance.",
    instruction="""
Check whether the AI system follows security and responsible AI best practices.
Return only the compliance findings.
"""
)