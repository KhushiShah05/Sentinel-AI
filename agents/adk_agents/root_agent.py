from google.adk.agents import Agent

from agents.adk_agents.prompt_agent import prompt_agent
from agents.adk_agents.security_agent import security_agent
from agents.adk_agents.hallucination_agent import hallucination_agent
from agents.adk_agents.evaluator_agent import evaluator_agent
from agents.adk_agents.report_agent import report_agent
from agents.adk_agents.compliance_agent import compliance_agent


root_agent = Agent(
    name="Sentinel_AI_Root_Agent",
    description="Coordinates all Sentinel AI security auditing agents.",
    instruction="""
You are the Root Agent for Sentinel AI.

Your responsibilities are:

1. Coordinate Prompt Injection analysis.
2. Coordinate Security analysis.
3. Coordinate Hallucination analysis.
4. Collect results.
5. Send all findings to the Evaluator Agent.
6. Produce one final security assessment.

Always delegate work to the appropriate specialized agent.
""",
    sub_agents=[
        prompt_agent,
        security_agent,
        hallucination_agent,
        evaluator_agent,
        compliance_agent,
        report_agent   
        ]
)