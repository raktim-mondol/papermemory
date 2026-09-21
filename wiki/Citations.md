# Citations

Non-negotiable:

1. Cite only papers returned by `papermemory cite` or `papermemory paper` (or the matching MCP tools).
2. Prefer `verified=1`. Hits with `verified: false` / `UNVERIFIED` are not confirmed metadata — say so.
3. If cite returns nothing, memory has no source. Do not invent a title, year, DOI, or bibtex key.
4. Run `cite-check` before treating a manuscript section as finished. Missing keys must be ingested or removed.

```bash
papermemory cite "attention-based multiple instance learning" --json
papermemory cite-check scandy --json
```

Claims stay `status=extracted` until the evidence quote is in the stored paper text. Do not mark `verified` without that check.

Coding-session memory (agentmemory, generic notes) is not a citation source.
