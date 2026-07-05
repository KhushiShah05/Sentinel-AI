import os
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import darkblue

class ReportAgent:
    def generate_pdf(
        self,
        pdf_path,
        prompt_results,
        security_results,
        hallucination_results,
        report,
        compliance_report
    ):
        styles = getSampleStyleSheet()

        title_style = styles["Heading1"]
        title_style.alignment = TA_CENTER
        title_style.textColor = darkblue

        heading = styles["Heading2"]
        normal = styles["BodyText"]

        doc = SimpleDocTemplate(pdf_path)
        story = []

        story.append(Paragraph("Sentinel AI Security Audit Report", title_style))
        story.append(
            Paragraph(
                f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                normal
            )
        )

        story.append(Spacer(1, 20))

        story.append(Paragraph("Prompt Injection", heading))
        for item in prompt_results:
            story.append(Paragraph(f"<b>Attack:</b> {item['attack']}", normal))
            story.append(Paragraph(f"<b>Status:</b> {item['status']}", normal))
            story.append(Spacer(1, 10))

        story.append(Paragraph("Security", heading))
        for item in security_results:
            story.append(Paragraph(f"<b>Attack:</b> {item['attack']}", normal))
            story.append(Paragraph(f"<b>Status:</b> {item['status']}", normal))
            story.append(Spacer(1, 10))

        story.append(Paragraph("Hallucination", heading))
        for item in hallucination_results:
            story.append(Paragraph(f"<b>Question:</b> {item['question']}", normal))
            story.append(Paragraph(f"<b>Status:</b> {item['status']}", normal))
            story.append(Spacer(1, 10))

        story.append(Paragraph("Compliance Summary", heading))
        for check, status in compliance_report.items():
            story.append(Paragraph(f"{check}: {status}", normal))

        story.append(Spacer(1, 20))

        story.append(Paragraph("Final Summary", heading))
        story.append(Paragraph(f"<b>Security Score:</b> {report['score']}/100", normal))
        story.append(Paragraph(f"<b>Total Vulnerabilities:</b> {report['vulnerabilities']}", normal))

        doc.build(story)

    def generate_report(
        self,
        prompt_results,
        security_results,
        hallucination_results,
        report,
        compliance_report
    ):
        os.makedirs("reports", exist_ok=True)
        report_path = "reports/audit_report.md"

        with open(report_path, "w", encoding="utf-8") as file:
            file.write("# Sentinel AI Report\n\n")
            file.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            file.write("---\n\n")

            file.write("## Prompt Injection\n\n")
            for item in prompt_results:
                file.write("### Attack\n")
                file.write(f"{item['attack']}\n\n")
                file.write("**Response:**\n")
                file.write(f"{item['response']}\n\n")
                file.write(f"**Status:** {item['status']}\n\n")
                file.write("---\n\n")

            file.write("## Security\n\n")
            for item in security_results:
                file.write("### Attack\n")
                file.write(f"{item['attack']}\n\n")
                file.write("**Response:**\n")
                file.write(f"{item['response']}\n\n")
                file.write(f"**Status:** {item['status']}\n\n")
                file.write("---\n\n")

            file.write("## Hallucination\n\n")
            for item in hallucination_results:
                file.write("### Question\n")
                file.write(f"{item['question']}\n\n")
                file.write("**Response:**\n")
                file.write(f"{item['response']}\n\n")
                file.write(f"**Status:** {item['status']}\n\n")
                file.write("---\n\n")

            file.write("## Compliance Summary\n\n")
            for check, status in compliance_report.items():
                symbol = "✅" if status == "PASS" else "❌"
                file.write(f"- {symbol} **{check}:** {status}\n")

            file.write("# 📊 Final Summary\n\n")
            file.write(f"**Security Score:** {report['score']}/100\n\n")
            file.write(f"**Total Vulnerabilities:** {report['vulnerabilities']}\n\n")

            if report["score"] >= 90:
                file.write("🟢 LOW RISK\n")
            elif report["score"] >= 70:
                file.write("🟡 MEDIUM RISK\n")
            else:
                file.write("🔴 HIGH RISK\n")

            file.write("\n---\n")
            file.write("# Recommendations\n\n")

            if report["vulnerabilities"] == 0:
                file.write("✅ No major vulnerabilities found.\n")
            else:
                file.write("- Improve Prompt Injection protection.\n")
                file.write("- Prevent secret leakage.\n")
                file.write("- Add hallucination guardrails.\n")

        pdf_path = "reports/audit_report.pdf"
        self.generate_pdf(
            pdf_path,
            prompt_results,
            security_results,
            hallucination_results,
            report,
            compliance_report
        )

        return {
           "markdown" :  report_path,
           "pdf" : pdf_path 
        } 
    
