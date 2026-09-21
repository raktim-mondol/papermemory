# Changelog

## 0.1.1 — 2026-09-21

- MCP stdio auto-detects newline-delimited JSON (current TypeScript MCP SDK, DeepSeek Harness, Grok) and LSP `Content-Length` headers.
- `papermemory ingest PATH --doi DOI` stores one verified paper (PDF + DOI on the same record).
- `papermemory ingest notes.md --pdf-path paper.pdf` merges markdown onto that paper.
- `--title` on ingest keeps a canonical title instead of an arXiv PDF header.
- Search index includes DOI and `pdf_path`.

## 0.1.0 — 2026-09-21

Initial release: SQLite academic memory, CLI, MCP server, and agent skill for ingest, search, cite, cite-check, recap, remember, claim, and lesson.
