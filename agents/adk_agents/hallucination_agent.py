from google.adk.agents import Agent
from agents.adk_agents.tools import run_hallucination_analysis

hallucination_agent = Agent(
    name="Hallucination_Agent",
    description="Detects hallucinations and unsupported claims.",
    instruction="""
You are the Hallucination Detection Agent.

Your responsibilities are:

- Detect hallucinated information
- Identify unsupported claims
- Flag fabricated facts
- Assess response reliability

Always use the provided tool.
Return only structured findings.
""",
    tools=[run_hallucination_analysis],
)