
# test_gemini.py

from agents.target_agent.agent import TargetAgent

agent = TargetAgent()

response = agent.ask(
    "You are a helpful career advisor.",
    "What is Python?"
)

print(response)