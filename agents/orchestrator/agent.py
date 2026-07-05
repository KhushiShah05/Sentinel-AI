from agents.prompt_injection.agent import PromptInjectionAgent
from agents.security.agent import SecurityAgent
from agents.hallucination.agent import HallucinationAgent
from agents.evaluator.agent import EvaluatorAgent
from agents.report.agent import ReportAgent
from agents.compliance.agent import ComplianceAgent
from memory.logger import log_audit
from agents.adk_agents.root_agent import root_agent


class OrchestratorAgent:

    def run_audit(self, system_prompt):

        adk_root = root_agent

        prompt_agent = PromptInjectionAgent()

        security_agent = SecurityAgent()

        hallucination_agent = HallucinationAgent()

        evaluator = EvaluatorAgent()

        report_agent = ReportAgent()

        prompt_results = prompt_agent.run_tests(
            system_prompt
        )

        security_results = security_agent.run_tests(
            system_prompt
        )

        hallucination_results = hallucination_agent.run_tests(
            system_prompt
        )

        report = evaluator.evaluate(
            prompt_results,
            security_results,
            hallucination_results
        )

        compliance_agent = ComplianceAgent()

        compliance_report = compliance_agent.check_compliance(
            prompt_results,
            security_results,
            hallucination_results
        )

        report_file_path = report_agent.generate_report(
            prompt_results,
            security_results,
            hallucination_results,
            report,
            compliance_report
        )
        print(report_file_path)

        result = {
            "prompt_results": prompt_results,
            "security_results": security_results,
            "hallucination_results": hallucination_results,
            "report": report,
            "compliance": compliance_report,
            "report_file_path": report_file_path
        }

        log_audit(result)

        return result