from agents.adk_agents.prompt_agent import prompt_agent
from agents.adk_agents.security_agent import security_agent
from agents.adk_agents.hallucination_agent import hallucination_agent
from agents.adk_agents.evaluator_agent import evaluator_agent

ADK_AGENTS = [
    prompt_agent,
    security_agent,
    hallucination_agent,
    evaluator_agent,
]