from google.adk.agents import Agent
from agents.adk_agents.tools import run_security_analysis

security_agent = Agent(
    name="Security_Agent",
    description="Analyzes security vulnerabilities in AI systems.",
    instruction="""
You are the Security Analysis Agent.

Your responsibilities include identifying:

- Sensitive data exposure
- Insecure coding patterns
- Missing input validation
- Prompt security risks

Always use the provided tool to perform the security analysis.
Return only structured findings.
""",
    tools=[run_security_analysis],
)