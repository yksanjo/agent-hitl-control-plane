# agent-hitl-control-plane

Human-in-the-loop control plane for approvals and escalation workflows.

## Scope

Review queues, approval states, and reversible action controls.

## Capabilities

- Review queues, approval states, and reversible action controls.
- SLA-aware routing for manual interventions and overrides.
- Decision capture with rationale, evidence, and audit context.
- Operator console APIs for multi-team governance workflows.

## Repository Layout

- `src/main.py` entrypoint and lightweight service bootstrap
- `src/project_profile.py` canonical project metadata
- `src/service_contract.py` baseline domain contract shape
- `tests/` smoke and contract tests
- `docs/` architecture and roadmap

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
pytest -q
python -m src.main
```
