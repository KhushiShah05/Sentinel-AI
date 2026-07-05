from google.adk.agents import Agent
from agents.adk_agents.tools import run_prompt_analysis

prompt_agent = Agent(
    name="Prompt_Injection_Agent",
    description="Detects prompt injection attacks against LLMs.",
    instruction="""
You are the Prompt Injection Security Agent.

Your job is to detect:

- Prompt Injection
- Jailbreak attacks
- System Prompt Leakage
- Instruction Override attacks

Whenever a prompt needs analysis, use the provided tool instead of making up results.
Return only the structured findings.
""",
    tools=[run_prompt_analysis],
)