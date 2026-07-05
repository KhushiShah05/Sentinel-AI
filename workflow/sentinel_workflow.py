from agents.prompt_injection.agent import PromptInjectionAgent
from agents.security.agent import SecurityAgent
from agents.hallucination.agent import HallucinationAgent
from agents.evaluator.agent import EvaluatorAgent
from agents.compliance.agent import ComplianceAgent
from agents.report.agent import ReportAgent


class SentinelWorkflow:

    def execute(self, system_prompt):

        prompt_results = PromptInjectionAgent().run_tests(system_prompt)

        security_results = SecurityAgent().run_tests(system_prompt)

        hallucination_results = HallucinationAgent().run_tests(system_prompt)

        report = EvaluatorAgent().evaluate(
            prompt_results,
            security_results,
            hallucination_results
        )

        compliance = ComplianceAgent().check_compliance(
            prompt_results,
            security_results,
            hallucination_results
        )

        report_path = ReportAgent().generate_report(
            prompt_results,
            security_results,
            hallucination_results,
            report,
            compliance
        )

        return {
            "prompt_results": prompt_results,
            "security_results": security_results,
            "hallucination_results": hallucination_results,
            "report": report,
            "compliance": compliance,
            "report_file_path": report_path
        }
    