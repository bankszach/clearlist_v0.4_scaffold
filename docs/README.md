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

## 🚀 AI Wisdom Agents with Semantic Intelligence
Transform profiles into **adaptive AI agents** that embody each teacher's wisdom:

- **🧠 Semantic Intelligence**: AI agents that understand question context and focus responses accordingly
- **🎯 Contextual Focusing**: Emphasizes relevant teachings, practices, or guidance based on what you ask
- **🎭 Adaptive Tone**: Sets emotional context (compassionate, direct, balanced) based on your needs
- **📊 Intelligent Sizing**: Optimizes response depth and prompt length for question complexity
- **🌐 Cross-Tradition Dialogue**: Explore different approaches to nondual insight with context-aware responses
- **⚡ Ready to Use**: Complete Python system with OpenAI integration and semantic focusing

### **What Makes This Special**
Unlike static AI chatbots, these agents **adapt their responses** based on your questions:
- Ask about practice → Get focused, step-by-step guidance
- Ask about philosophy → Get theoretical insights and core claims
- Ask for help with struggles → Get compassionate, supportive responses
- Ask for direct answers → Get clear, immediate guidance

See `README_demo.md` for full AI agent documentation and setup.
