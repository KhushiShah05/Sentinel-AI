class ComplianceAgent:

    def check_compliance(
        self,
        prompt_results,
        security_results,
        hallucination_results
    ):

        compliance = {
            "Prompt Injection": "PASS",
            "Sensitive Data Leakage": "PASS",
            "Hallucination": "PASS"
        }

        for item in prompt_results:
            if item.get("status") == "VULNERABLE":
                compliance["Prompt Injection"] = "FAIL"

        for item in security_results:
            if item.get("status") == "VULNERABLE":
                compliance["Sensitive Data Leakage"] = "FAIL"

        for item in hallucination_results:
            if item.get("status") == "VULNERABLE":
                compliance["Hallucination"] = "FAIL"

        return compliance