# Paper 2 Multi-Agent Demo

This folder contains a implementation inspired by:
**"Orchestral AI: A Framework for Agent Orchestration" (arXiv:2601.02577v1).**

## What this demo does

It implements an **AI software feature planning assistant**.

Input:
- A feature request (GitHub-issue style text)

Output:
- A structured engineering brief with:
  - clarified requirements
  - architecture suggestions
  - testing strategy
  - risks / open questions
  - recommended next steps

## How this maps to Paper 2

This demo explicitly reflects the paper's core ideas:
- **Agent architecture (LLM + tools + context):** each agent has a role, tools, and local context.
- **Specialized subagents:** three worker agents focus on requirements, architecture, and QA.
- **Hierarchical coordination:** one manager agent delegates tasks to workers and synthesizes final output.
- **Provider-agnostic pattern:** workers depend on an `LLMProvider` interface (default is an offline deterministic provider).
- **Traceability / cost awareness:** tool calls and delegations are logged with estimated token counts.

## Files

- `paper2_multi_agent_demo.py`: main runnable script
- `sample_output.md`: example output structure

## Setup

Requirements:
- Python 3.10+

No extra dependencies are required.

## Run

From repo root:

```bash
python paper2_multi_agent_demo/paper2_multi_agent_demo.py
```

Equivalent explicit provider form:

```bash
python paper2_multi_agent_demo/paper2_multi_agent_demo.py --provider offline
```

Run with a custom request:

```bash
python paper2_multi_agent_demo/paper2_multi_agent_demo.py \
  --feature-request "Add MFA login with backup codes and trusted devices."
```

Run using a text file as input:

```bash
python paper2_multi_agent_demo/paper2_multi_agent_demo.py --input-file path/to/issue.txt
```

Print only (no saved artifact):

```bash
python paper2_multi_agent_demo/paper2_multi_agent_demo.py --no-save
```

By default, output is saved to:
- `paper2_multi_agent_demo/artifacts/latest_engineering_brief.md`

.
