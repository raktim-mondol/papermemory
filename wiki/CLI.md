# CLI

`papermemory` is the command. Pass `--json` before or after the subcommand for agents.

```bash
papermemory init
papermemory ingest PATH --project SLUG --json
papermemory ingest PATH --doi DOI --project SLUG --json
papermemory ingest notes.md --pdf-path paper.pdf --json
papermemory ingest --arxiv 1706.03762 --project SLUG --json
papermemory ingest --doi 10.1038/s41592-024-02201-0

papermemory search "query" --kind all --limit 8 --json
papermemory paper BIBKEY --json
papermemory understand BIBKEY --save
papermemory cite "statement" --json
papermemory cite-check SLUG --json
papermemory recap --project SLUG --json
papermemory remember "decision" --concepts a,b --project SLUG --json
papermemory lesson "rule" --concepts citations --json
papermemory claim "text" --paper ID --evidence QUOTE --status extracted --json
papermemory verify KEY
papermemory doctor --json
papermemory mcp
```

`--kind` on ingest: `auto`, `pdf`, `bibtex`, `markdown`, `tex`, `dir`, `manuscript`.

See [[Ingest]] for DOI merge and [[MCP]] for the stdio server.
