# Changelog

## 0.2.1 — 2026-10-22

- `papermemory ingest --cwd PATH` resolves the project from the workspace: explicit project → nearest `ah.yaml` ancestor → manuscript `root_path` → `unassigned`.
- Explicit `--project` values are slugified (`"My Paper"` → `my-paper`) and win over `--cwd`.
- MCP `papermemory_ingest` accepts `cwd` and resolves the same way.
- Auto-ingest callers pass the workspace `cwd`; `PAPERMEMORY_PROJECT` remains the explicit override.
- Added CLI/MCP project-resolution tests (`tests/test_scope_wiring.py`).

## 0.1.1 — 2026-09-21

- MCP stdio auto-detects newline-delimited JSON (current TypeScript MCP SDK, DeepSeek Harness, Grok) and LSP `Content-Length` headers.
- `papermemory ingest PATH --doi DOI` stores one verified paper (PDF + DOI on the same record).
- `papermemory ingest notes.md --pdf-path paper.pdf` merges markdown onto that paper.
- `--title` on ingest keeps a canonical title instead of an arXiv PDF header.
- Search index includes DOI and `pdf_path`.

## 0.1.0 — 2026-09-21

Initial release: SQLite academic memory, CLI, MCP server, and agent skill for ingest, search, cite, cite-check, recap, remember, claim, and lesson.
