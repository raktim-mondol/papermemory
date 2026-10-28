# Changelog

## Unreleased (0.3.0, in progress)

Reference library, phase 1 (lossless records and import). Schema 2000 → 2100; run `papermemory migrate` (back up first).

- New additive tables: `reference_meta`, `bib_keys`, `bib_key_aliases`, `paper_tags`, `collections`, `collection_papers`, `integrity`. `papers` is not altered, and existing `bibtex_key` values are never changed. Existing papers are backfilled.
- New tolerant BibTeX/BibLaTeX parser (`bibparse.py`): `@string` macros, `#` concatenation, `()` entries, escaped quotes, month macros, braced corporate authors, duplicate fields. **Fixes silent data loss:** an entry with a missing closing brace used to swallow the next entry (and give it the wrong title); it is now reported and recovered.
- RIS (`ris.py`) and CSL-JSON (`csl_import.py`) readers. `papermemory library import PATH|-` with `--format`, `--project`, `--cwd`, `--dry-run`, `--batch-size`; `papermemory library get REF`.
- Imports are lossless (CSL-JSON plus every unmapped field under its original name, plus the verbatim BibTeX entry), idempotent, batched, and never abort on one bad entry.
- Library-wide unique citation keys; a key owned by a different paper gets a letter suffix; the key a project used is stored as a project alias. `cite-check` resolves project aliases.
- `merge_papers` carries library rows (record, keys, aliases, tags, collections, integrity) to the surviving paper.
- JSONL export/restore include the new tables (`pm-2.1`; `pm-2` exports still restore).
- `.ris` files are recognised by `ingest`.
- Reference library, phase 2 (citation keys): `library keys check|assign|freeze|rekey`. Key template (`{family}{year}{titleword}` default; `{doi}` and `{arxiv}` tokens; `PAPERMEMORY_KEY_TEMPLATE`), BibTeX-safe cleanup, DOI/arXiv fallback for records with no author or year. Keys are set once; `freeze` records that a key is relied on; `rekey` is a dry run unless `--apply` with a reason, lists the manuscripts that cite the old key, and keeps it as a library-wide alias that `cite-check` resolves. New audit ops `KEY_FREEZE` and `KEY_RENAME`.
- Reference library, phase 3 (organisation and query): tags, collections (one level of nesting, optional project and `.bib` binding, ordered), per-paper notes (paper-scoped observations; edits keep the old text), a filter syntax with an unknown-field error, and `library list` with keyset paging, sorting, and `total_count`. Tags and notes are included in paper search. `merge_papers` keeps tags and collection membership. New CLI: `library list|tag|collection|note`.

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
