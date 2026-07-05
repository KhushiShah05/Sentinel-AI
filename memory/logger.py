import json
from datetime import datetime


def log_event(agent_name, action):
    event = {
        "timestamp": str(datetime.now()),
        "agent": agent_name,
        "action": action
    }

    with open(
        "memory/audit_log.json",
        "a",
        encoding="utf-8"
    ) as f:
        f.write(json.dumps(event) + "\n")


def log_audit(result):
    audit = {
        "timestamp": str(datetime.now()),
        "score": result["report"]["score"],
        "vulnerabilities": result["report"]["vulnerabilities"],
        "prompt_results": result["prompt_results"],
        "security_results": result["security_results"],
        "hallucination_results": result["hallucination_results"],
        "compliance": result.get("compliance", {})
    }

    with open(
        "memory/audit_log.json",
        "a",
        encoding="utf-8"
    ) as f:
        f.write(json.dumps(audit) + "\n")