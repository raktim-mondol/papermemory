# MCP

```bash
papermemory mcp
```

## Framing

The server detects the first inbound message:

- **NDJSON** — one JSON-RPC object per line (TypeScript MCP SDK, DeepSeek Harness, recent Grok)
- **Content-Length** — LSP-style headers (older clients)

Replies use the same framing. v0.1.0 Content-Length-only servers deadlock NDJSON clients.

## Grok

```toml
[mcp_servers.papermemory]
command = "papermemory"
args = ["mcp"]
```

## Tools

| Tool | Role |
| --- | --- |
| `papermemory_search` | Hybrid search over papers, claims, chunks, notes, lessons |
| `papermemory_ingest` | Path, arXiv, DOI; `path` may be combined with `doi`, `title`, `pdf_path` |
| `papermemory_get` | Paper by id or bibtex key |
| `papermemory_cite` | Citable paper for a statement |
| `papermemory_cite_check` | Manuscript in-text keys vs memory |
| `papermemory_remember` | Writing/reading decision |
| `papermemory_claim` | Claim with optional evidence |
| `papermemory_recap` | Project briefing |
| `papermemory_lesson` | Durable rule |

ResearchCraft mounts these as `mcp__papermemory__*` on its ResearchCraft preset. See [[ResearchCraft]].
