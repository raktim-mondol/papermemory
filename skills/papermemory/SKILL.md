---
name: papermemory
description: >
  Academic paper memory for understanding papers and writing papers. Use for
  literature, citations, claims, manuscripts, related work, bibtex, DOI/arXiv
  ingest, cite-check, and recap of a writing project. Triggers: paper memory,
  remember this paper, cite this, citation check, literature review, manuscript
  status, /papermemory. Not for coding-session memory.
user-invocable: true
argument-hint: "[recap|search|ingest|cite|cite-check|remember] [query or path]"
---

# PaperMemory

Local academic memory. CLI: `papermemory`. Prefer `--json`. Database: `~/.local/share/papermemory/papermemory.db`.

If MCP tools `papermemory_*` are available, use those instead of the CLI.

## First action

On any paper-writing or paper-reading task, run:

```bash
papermemory recap --json --project <slug>
```

Slug examples: `scandy` for `~/journal_paper_writing`, `breast-imaging` for `~/breast_imaging_ai_review`. If the slug is unknown, `papermemory recap --json`.

## Commands

| Goal | Command |
| --- | --- |
| Ingest a manuscript tree | `papermemory ingest PATH --kind manuscript --project SLUG --json` |
| Ingest PDF / bib / markdown | `papermemory ingest PATH --project SLUG --json` |
| Ingest arXiv / DOI | `papermemory ingest --arxiv ID --project SLUG --json` / `--doi DOI` |
| Search | `papermemory search QUERY --json` |
| Show a paper | `papermemory paper BIBKEY --json` |
| Find a citation | `papermemory cite QUERY --json` |
| Check manuscript cites | `papermemory cite-check SLUG --json` |
| Save a decision | `papermemory remember TEXT --concepts a,b --project SLUG --json` |
| Save a durable rule | `papermemory lesson TEXT --concepts a,b --json` |
| Store a claim | `papermemory claim TEXT --paper ID --evidence QUOTE --status extracted --json` |

## Citation integrity

- Cite only papers returned by `papermemory cite` or `papermemory paper`.
- If the hit is `verified: false` / `UNVERIFIED`, say so and do not treat the metadata as confirmed.
- If cite returns no hits, say that memory has no source. Do not invent a title, year, DOI, or bibtex key.
- Before finishing a section, run `cite-check`. Missing keys must be ingested or removed, not guessed.

## Understanding a paper

1. `ingest` the PDF or arXiv/DOI.
2. `paper KEY` for metadata, stored claims, chunks.
3. Read the PDF/chunks. Save claims with an evidence quote and `status=extracted` until the quote is checked.
4. `remember` the reading notes tagged with the bibtex key.

## Writing a paper

1. `recap --project SLUG` for venue, citation style, section word counts, open reviewer comments, terminology.
2. Search claims/papers before writing related work.
3. `remember` outline decisions and rejected phrasings.
4. `cite-check` before calling a section done.

## Do not

- Do not use coding-agent memory (agentmemory, generic session notes) as the source of citations.
- Do not mark a claim `verified` unless the evidence quote is in the stored paper text.
