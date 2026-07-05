from agents.prompt_injection.agent import PromptInjectionAgent
from agents.security.agent import SecurityAgent
from agents.hallucination.agent import HallucinationAgent


def run_prompt_analysis(system_prompt: str):
    """
    Runs Prompt Injection analysis.
    """
    return PromptInjectionAgent().run_tests(system_prompt)


def run_security_analysis(system_prompt: str):
    """
    Runs Security analysis.
    """
    return SecurityAgent().run_tests(system_prompt)


def run_hallucination_analysis(system_prompt: str):
    """
    Runs Hallucination analysis.
    """
    return HallucinationAgent().run_tests(system_prompt)