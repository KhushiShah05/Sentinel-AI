from agents.orchestrator.agent import OrchestratorAgent

agent = OrchestratorAgent()

system_prompt = """
You are a helpful career advisor.
"""

result = agent.run_audit(system_prompt)

print("\n========== SENTINEL AI REPORT ==========\n")

print("PROMPT INJECTION RESULTS")
for item in result["prompt_results"]:
    print(item["status"], "-", item["attack"])

print("\nSECURITY RESULTS")
for item in result["security_results"]:
    print(item["status"], "-", item["attack"])

print("\nHALLUCINATION RESULTS")
for item in result["hallucination_results"]:
    print(item["status"], "-", item["question"])

print("\nFINAL REPORT")
print(result["report"])
print(result["security_results"])
print(result["hallucination_results"])