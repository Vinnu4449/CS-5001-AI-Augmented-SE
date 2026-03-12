# Sample Output Structure

```markdown
# Engineering Brief: AI Software Feature Planning Assistant

## Input Feature Request
Build a feature that lets users reset their password by email...

## 1) Clarified Requirements
### Functional Requirements
- ...

### Non-Functional Considerations
- ...

### Requirement Analyst Summary
- ...

## 2) Proposed Architecture
### Components
- ...

### Implementation Flow
- ...

### Architecture Planner Notes
- ...

## 3) Testing Strategy
### Unit Tests
- ...

### Integration Tests
- ...

### Security Tests
- ...

### QA Acceptance Criteria
- ...

## 4) Risks / Open Questions
- ...

## 5) Recommended Next Steps
- ...

## 6) Traceability Metadata
{
  "provider": "rule-based-offline",
  "generated_at_utc": "...",
  "estimated_total_tokens": 0,
  "events_logged": 0
}

### Delegation + Tool Call Trace
- [delegation] manager -> delegate (requirements_analyst)
- [tool_call] requirements_analyst -> extract_functional_requirements
- ...
```

Generate a real run artifact with:
- `python paper2_multi_agent_demo/paper2_multi_agent_demo.py`
- Output file: `paper2_multi_agent_demo/artifacts/latest_engineering_brief.md`
