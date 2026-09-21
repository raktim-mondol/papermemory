# PaperMemory wiki

Persistent **local** academic memory for reading and writing papers. SQLite + FTS5. No cloud.

**Repo:** https://github.com/raktim-mondol/papermemory  
**Install:** `pip install "papermemory[pdf] @ git+https://github.com/raktim-mondol/papermemory.git"`

## Guides

- [[Install]]
- [[CLI]]
- [[MCP]]
- [[Ingest]]
- [[Citations]]
- [[ResearchCraft]]

## What it stores

| Kind | Examples |
| --- | --- |
| Papers | title, authors, year, venue, DOI, arXiv, bibtex key, verified flag |
| Evidence | claims with quoted evidence, page/section |
| Graph | cites / extends / contradicts / uses-method |
| Writing | manuscripts, section word counts, contributions, terminology, reviewer comments |
| Integrity | cite-check against in-text keys |

Default database: `~/.local/share/papermemory/papermemory.db` (`PAPERMEMORY_DB` or `PAPERMEMORY_DATA_DIR` to override).

Current release: **v0.1.1**.
