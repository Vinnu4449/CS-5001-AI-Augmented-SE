#!/usr/bin/env python3
"""Paper 2 inspired multi-agent demo: AI software feature planning assistant."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable, Dict, List, Protocol

DEFAULT_FEATURE_REQUEST = (
    "Build a feature that lets users reset their password by email. "
    "The system should send a time-limited reset link, prevent token reuse, "
    "log reset attempts, and show clear error messages for expired or invalid links."
)


class LLMProvider(Protocol):
    """Provider-agnostic LLM interface used by all agents."""

    name: str

    def complete(self, *, system_prompt: str, user_prompt: str, context: Dict[str, Any]) -> str:
        ...


class RuleBasedProvider:
    """Deterministic offline provider so the demo runs without external APIs."""

    name = "rule-based-offline"

    def complete(self, *, system_prompt: str, user_prompt: str, context: Dict[str, Any]) -> str:
        bullets = context.get("bullets", [])
        if bullets:
            return "\n".join(f"- {item}" for item in bullets)
        return user_prompt.strip()


@dataclass
class TraceEvent:
    timestamp_utc: str
    event_type: str
    actor: str
    action: str
    details: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TraceLogger:
    events: List[TraceEvent] = field(default_factory=list)

    def log(self, event_type: str, actor: str, action: str, **details: Any) -> None:
        self.events.append(
            TraceEvent(
                timestamp_utc=datetime.now(timezone.utc).isoformat(),
                event_type=event_type,
                actor=actor,
                action=action,
                details=details,
            )
        )

    def total_estimated_tokens(self) -> int:
        total = 0
        for event in self.events:
            total += int(event.details.get("estimated_tokens", 0))
        return total


def estimate_tokens(value: Any) -> int:
    if isinstance(value, str):
        text = value
    else:
        text = json.dumps(value, sort_keys=True)
    return max(1, len(re.findall(r"\w+", text)))


class BaseAgent:
    def __init__(self, name: str, role_prompt: str, provider: LLMProvider, trace: TraceLogger):
        self.name = name
        self.role_prompt = role_prompt
        self.provider = provider
        self.trace = trace
        self.context: Dict[str, Any] = {"agent": name, "role": role_prompt, "provider": provider.name}
        self.tools: Dict[str, Callable[..., Any]] = {}

    def register_tool(self, name: str, fn: Callable[..., Any]) -> None:
        self.tools[name] = fn

    def call_tool(self, tool_name: str, **kwargs: Any) -> Any:
        result = self.tools[tool_name](**kwargs)
        token_cost = estimate_tokens(kwargs) + estimate_tokens(result)
        self.trace.log(
            "tool_call",
            actor=self.name,
            action=tool_name,
            input=kwargs,
            output=result,
            estimated_tokens=token_cost,
        )
        return result


class RequirementsAnalystAgent(BaseAgent):
    def __init__(self, provider: LLMProvider, trace: TraceLogger):
        super().__init__(
            name="requirements_analyst",
            role_prompt="Clarify product requirements and identify ambiguities.",
            provider=provider,
            trace=trace,
        )
        self.register_tool("extract_functional_requirements", self.extract_functional_requirements)
        self.register_tool("extract_non_functional", self.extract_non_functional)
        self.register_tool("identify_open_questions", self.identify_open_questions)

    def extract_functional_requirements(self, feature_request: str) -> List[str]:
        requirements: List[str] = []
        clauses = [c.strip() for c in re.split(r"[.;]", feature_request) if c.strip()]

        for clause in clauses:
            cleaned = clause[0].upper() + clause[1:]
            if cleaned.lower().startswith("build a feature"):
                cleaned = cleaned.replace("Build a feature that ", "")
            if cleaned and cleaned[0].islower():
                cleaned = cleaned[0].upper() + cleaned[1:]
            requirements.append(cleaned)

        normalized = feature_request.lower()
        if "password" in normalized and "email" in normalized:
            requirements.append("Users request password reset using a registered email address")
        if "time-limited" in normalized:
            requirements.append("Reset token has explicit expiration time and is validated on use")
        if "prevent token reuse" in normalized:
            requirements.append("Token is invalidated immediately after successful reset")

        deduped = []
        seen = set()
        for req in requirements:
            key = req.lower()
            if key not in seen:
                seen.add(key)
                deduped.append(req)
        return deduped

    def extract_non_functional(self, feature_request: str) -> List[str]:
        concerns: List[str] = []
        normalized = feature_request.lower()

        if "log" in normalized:
            concerns.append("Auditability: log reset requests, token validations, and completion outcomes")
        concerns.append("Security: use single-use, high-entropy tokens and avoid leaking token values in logs")
        concerns.append("Usability: show clear, actionable error messages for invalid/expired links")
        concerns.append("Reliability: handle email delivery failures and retry policies")
        concerns.append("Privacy: avoid user enumeration in reset request responses")
        return concerns

    def identify_open_questions(self, feature_request: str) -> List[str]:
        return [
            "What token lifetime is required (e.g., 15 minutes vs 1 hour)?",
            "Should password reset enforce recent-password reuse checks?",
            "Do we need rate limits by IP, email, or both?",
            "What audit retention policy is required for reset logs?",
        ]

    def run(self, feature_request: str) -> Dict[str, Any]:
        functional = self.call_tool("extract_functional_requirements", feature_request=feature_request)
        non_functional = self.call_tool("extract_non_functional", feature_request=feature_request)
        questions = self.call_tool("identify_open_questions", feature_request=feature_request)

        summary = self.provider.complete(
            system_prompt=self.role_prompt,
            user_prompt="Summarize requirement analysis.",
            context={"bullets": [f"{len(functional)} functional requirements captured", f"{len(questions)} open questions identified"]},
        )

        return {
            "functional_requirements": functional,
            "non_functional_considerations": non_functional,
            "open_questions": questions,
            "summary": summary,
        }


class ArchitecturePlannerAgent(BaseAgent):
    def __init__(self, provider: LLMProvider, trace: TraceLogger):
        super().__init__(
            name="architecture_planner",
            role_prompt="Propose implementation architecture and delivery approach.",
            provider=provider,
            trace=trace,
        )
        self.register_tool("propose_components", self.propose_components)
        self.register_tool("propose_flow", self.propose_flow)
        self.register_tool("identify_risks", self.identify_risks)

    def propose_components(self, feature_request: str, requirements: List[str]) -> List[str]:
        return [
            "`Auth API` endpoint: `POST /password-reset/request` and `POST /password-reset/confirm`",
            "`Token Service`: generate, hash, store expiry, enforce single-use semantics",
            "`Email Service`: send reset template with signed reset URL",
            "`Audit Logger`: structured events for request, validation, and completion",
            "`UI Screens`: request form, reset form, and error state pages",
        ]

    def propose_flow(self, requirements: List[str]) -> List[str]:
        return [
            "User submits email to request reset",
            "System returns generic success response (prevents account enumeration)",
            "Token service creates expiring single-use token and stores hashed value",
            "Email service sends reset link containing opaque token",
            "User opens link, backend validates token freshness + single-use state",
            "On valid token, user sets new password and token is consumed",
            "Audit logger records every stage with correlation ID",
        ]

    def identify_risks(self, requirements: List[str]) -> List[str]:
        return [
            "Replay attacks if token invalidation is not atomic",
            "User confusion if expired-link messaging is unclear",
            "Operational risk if email provider latency is high",
            "Security risk if reset links are logged in plaintext",
        ]

    def run(self, feature_request: str, requirements_summary: Dict[str, Any]) -> Dict[str, Any]:
        components = self.call_tool(
            "propose_components",
            feature_request=feature_request,
            requirements=requirements_summary["functional_requirements"],
        )
        flow = self.call_tool("propose_flow", requirements=requirements_summary["functional_requirements"])
        risks = self.call_tool("identify_risks", requirements=requirements_summary["functional_requirements"])

        implementation_notes = self.provider.complete(
            system_prompt=self.role_prompt,
            user_prompt="Summarize architecture decisions.",
            context={
                "bullets": [
                    "Use stateless APIs with persistent token state",
                    "Prioritize security controls around token lifecycle",
                    "Add structured audit events for traceability",
                ]
            },
        )

        return {
            "proposed_components": components,
            "implementation_flow": flow,
            "architecture_risks": risks,
            "implementation_notes": implementation_notes,
        }


class QATestStrategyAgent(BaseAgent):
    def __init__(self, provider: LLMProvider, trace: TraceLogger):
        super().__init__(
            name="qa_test_strategy",
            role_prompt="Design practical testing and validation strategy.",
            provider=provider,
            trace=trace,
        )
        self.register_tool("unit_tests", self.unit_tests)
        self.register_tool("integration_tests", self.integration_tests)
        self.register_tool("security_tests", self.security_tests)

    def unit_tests(self, requirements_summary: Dict[str, Any]) -> List[str]:
        return [
            "Token generation creates high-entropy values and stores hash only",
            "Expired token is rejected at validation layer",
            "Consumed token cannot be reused",
            "Error mapper returns deterministic user-facing messages",
        ]

    def integration_tests(self, architecture_summary: Dict[str, Any]) -> List[str]:
        return [
            "End-to-end happy path from reset request to password update",
            "Expired-link flow returns correct UI and backend status",
            "Invalid token flow logs audit event and blocks password update",
            "Email send failure path triggers retry/failure handling",
        ]

    def security_tests(self, feature_request: str) -> List[str]:
        return [
            "Brute-force/rate-limit checks for reset endpoint",
            "No user enumeration through response body or timing",
            "Token replay attempts are rejected and audited",
            "Logs and telemetry do not leak raw tokens",
        ]

    def run(
        self,
        feature_request: str,
        requirements_summary: Dict[str, Any],
        architecture_summary: Dict[str, Any],
    ) -> Dict[str, Any]:
        unit = self.call_tool("unit_tests", requirements_summary=requirements_summary)
        integration = self.call_tool("integration_tests", architecture_summary=architecture_summary)
        security = self.call_tool("security_tests", feature_request=feature_request)

        acceptance_criteria = self.provider.complete(
            system_prompt=self.role_prompt,
            user_prompt="Summarize release readiness gates.",
            context={
                "bullets": [
                    "All critical security tests pass",
                    "Core reset flow and failure paths covered by integration tests",
                    "Audit logs validated in staging",
                ]
            },
        )

        return {
            "unit_test_plan": unit,
            "integration_test_plan": integration,
            "security_test_plan": security,
            "acceptance_criteria": acceptance_criteria,
        }


class EngineeringManagerAgent:
    def __init__(self, provider: LLMProvider):
        self.trace = TraceLogger()
        self.provider = provider
        self.requirements_agent = RequirementsAnalystAgent(provider, self.trace)
        self.architecture_agent = ArchitecturePlannerAgent(provider, self.trace)
        self.qa_agent = QATestStrategyAgent(provider, self.trace)

    def delegate(self, worker_name: str, task_description: str) -> None:
        self.trace.log(
            "delegation",
            actor="manager",
            action="delegate",
            worker=worker_name,
            task=task_description,
            estimated_tokens=estimate_tokens(task_description),
        )

    def create_engineering_brief(self, feature_request: str) -> str:
        # Manager orchestrates specialized subagents and synthesizes their outputs,
        # following Paper 2's hierarchical coordination pattern.
        self.delegate("requirements_analyst", "Clarify requirements and ambiguities")
        req = self.requirements_agent.run(feature_request)

        self.delegate("architecture_planner", "Propose architecture from requirements")
        arch = self.architecture_agent.run(feature_request, req)

        self.delegate("qa_test_strategy", "Build test strategy from requirements and architecture")
        qa = self.qa_agent.run(feature_request, req, arch)

        risks = list(dict.fromkeys(arch["architecture_risks"] + req["open_questions"]))

        next_steps = [
            "Confirm open requirement decisions (token TTL, rate limits, retention policy)",
            "Implement API endpoints and token lifecycle with atomic consume semantics",
            "Integrate email provider + templates and add observability hooks",
            "Ship test suite and run security checks before release",
        ]

        trace_lines = []
        for idx, event in enumerate(self.trace.events, start=1):
            summary = f"{idx}. [{event.event_type}] {event.actor} -> {event.action}"
            if event.event_type == "delegation":
                summary += f" ({event.details.get('worker')})"
            trace_lines.append(summary)

        metadata = {
            "provider": self.provider.name,
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "estimated_total_tokens": self.trace.total_estimated_tokens(),
            "events_logged": len(self.trace.events),
        }

        return "\n".join(
            [
                "# Engineering Brief: AI Software Feature Planning Assistant",
                "",
                "## Input Feature Request",
                feature_request,
                "",
                "## 1) Clarified Requirements",
                "### Functional Requirements",
                *[f"- {item}" for item in req["functional_requirements"]],
                "",
                "### Non-Functional Considerations",
                *[f"- {item}" for item in req["non_functional_considerations"]],
                "",
                "### Requirement Analyst Summary",
                req["summary"],
                "",
                "## 2) Proposed Architecture",
                "### Components",
                *[f"- {item}" for item in arch["proposed_components"]],
                "",
                "### Implementation Flow",
                *[f"- {item}" for item in arch["implementation_flow"]],
                "",
                "### Architecture Planner Notes",
                arch["implementation_notes"],
                "",
                "## 3) Testing Strategy",
                "### Unit Tests",
                *[f"- {item}" for item in qa["unit_test_plan"]],
                "",
                "### Integration Tests",
                *[f"- {item}" for item in qa["integration_test_plan"]],
                "",
                "### Security Tests",
                *[f"- {item}" for item in qa["security_test_plan"]],
                "",
                "### QA Acceptance Criteria",
                qa["acceptance_criteria"],
                "",
                "## 4) Risks / Open Questions",
                *[f"- {item}" for item in risks],
                "",
                "## 5) Recommended Next Steps",
                *[f"- {item}" for item in next_steps],
                "",
                "## 6) Traceability Metadata",
                "```json",
                json.dumps(metadata, indent=2),
                "```",
                "",
                "### Delegation + Tool Call Trace",
                *[f"- {line}" for line in trace_lines],
                "",
            ]
        )


def resolve_feature_request(args: argparse.Namespace) -> str:
    if args.input_file:
        return Path(args.input_file).read_text(encoding="utf-8").strip()
    return args.feature_request.strip()


def resolve_output_path(script_dir: Path, requested_path: str) -> Path:
    output_path = Path(requested_path)
    if not output_path.is_absolute():
        output_path = script_dir / output_path
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Paper 2 inspired multi-agent feature planning demo")
    parser.add_argument("--feature-request", default=DEFAULT_FEATURE_REQUEST, help="Feature request text")
    parser.add_argument("--input-file", help="Optional file path containing the feature request")
    parser.add_argument(
        "--provider",
        default="offline",
        choices=["offline"],
        help="Provider to use for this demo",
    )
    parser.add_argument(
        "--output-file",
        default="artifacts/latest_engineering_brief.md",
        help="Where to save markdown output (relative paths resolve from script directory)",
    )
    parser.add_argument("--no-save", action="store_true", help="Print output only")
    args = parser.parse_args()

    feature_request = resolve_feature_request(args)
    provider = RuleBasedProvider()
    manager = EngineeringManagerAgent(provider=provider)
    brief = manager.create_engineering_brief(feature_request)

    print("=" * 88)
    print("FEATURE REQUEST")
    print("=" * 88)
    print(feature_request)
    print()
    print("=" * 88)
    print("ENGINEERING BRIEF")
    print("=" * 88)
    print(brief)

    if not args.no_save:
        script_dir = Path(__file__).resolve().parent
        output_path = resolve_output_path(script_dir, args.output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(brief, encoding="utf-8")
        print()
        print(f"Saved brief to: {output_path}")


if __name__ == "__main__":
    main()
