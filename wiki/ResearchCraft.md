# ResearchCraft

[dsh-researchcraft](https://github.com/raktim-mondol/dsh-researchcraft) **0.8.2+** vendors PaperMemory. Installing the plugin is enough:

```bash
dsh plugin --profile researchcraft add github:raktim-mondol/dsh-researchcraft
```

On first ResearchCraft start the plugin installs the CLI into `~/.dsh/papermemory` and mounts `mcp__papermemory__*` on the ResearchCraft preset. No API key.

`paper_download` ingests the PDF with its DOI. `pdf_to_markdown` with `write_to` merges markdown onto that same paper.

The SQLite file is still `~/.local/share/papermemory/papermemory.db`, so Grok and the CLI see the same store.

Override: `PAPERMEMORY_CLI`, `PAPERMEMORY_DB`, `PAPERMEMORY_PROJECT`, `PAPERMEMORY_SKIP_INSTALL=1`.
