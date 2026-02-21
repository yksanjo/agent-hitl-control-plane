# Architecture

## Goal

Human-in-the-loop control plane for approvals and escalation workflows.

## Core Components

1. Ingress interface for requests and task metadata
2. Policy and validation layer for deterministic control
3. Domain service core for business logic execution
4. Output adapters for events, persistence, and telemetry

## Design Notes

- Keep core logic deterministic and side-effect aware.
- Emit structured telemetry for every execution path.
- Make policy decisions explicit and auditable.
- Separate contract definitions from runtime adapters.
