# CLEARLIST — Nondual Index & AI Wisdom Agents (v0.4)

Neutral, cross‑tradition index of people associated with nondual insight.
Each person = one JSON **capsule** in `profiles/` (<5KB) that can be brought to life as an AI agent.
Links come later in `links/edges.json`.

## Layout
- `profiles/` — one file per person
- `links/edges.json` — cross‑references added later
- `sources/bibliography.json` — optional shared sources
- `schemas/` — JSON Schemas for validation
- `manifests/index.json` — list of available profiles + hashes
- `media/` — licensed assets (optional)
- `docs/` — style and contributor guides

## Quick start
1. Add or edit a `profiles/*.json` using `schemas/profile.schema.json`.
2. Run validation (example): `jq . profiles/*.json` then a JSON‑Schema validator.
3. Update `manifests/index.json` (hashes) — or run the provided script in your toolchain.
4. Add links later to `links/edges.json`.

## 🚀 AI Wisdom Agents
Transform profiles into interactive AI agents that embody each teacher's wisdom:
- **Interactive Conversations**: Chat with spiritual teachers in their authentic voice
- **Rich Context**: AI responses draw from documented teachings, practices, and claims
- **Cross-Tradition Dialogue**: Explore different approaches to nondual insight
- **Ready to Use**: Complete Python system with OpenAI integration

See `README_demo.md` for full AI agent documentation and setup.
