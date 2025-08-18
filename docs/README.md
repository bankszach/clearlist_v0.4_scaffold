# CLEARLIST — Nondual Index (v0.4)

Neutral, cross‑tradition index of people associated with nondual insight.
Each person = one JSON **capsule** in `profiles/` (<5KB). Links come later in `links/edges.json`.

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
