# Install

Requires Python 3.10+.

```bash
pip install "papermemory[pdf] @ git+https://github.com/raktim-mondol/papermemory.git"
papermemory init
```

The `[pdf]` extra installs `pypdf` for local PDF ingest.

Editable checkout:

```bash
git clone https://github.com/raktim-mondol/papermemory.git
cd papermemory
pip install -e '.[pdf,dev]'
pytest
```

## Environment

| Variable | Purpose |
| --- | --- |
| `PAPERMEMORY_DB` | Full path to the SQLite file |
| `PAPERMEMORY_DATA_DIR` | Directory for the default `papermemory.db` |

Default store: `~/.local/share/papermemory/papermemory.db`. A standalone CLI, Grok, and [ResearchCraft](https://github.com/raktim-mondol/dsh-researchcraft) share this file when they use the default path.

## Agent skill

Copy `skills/papermemory/SKILL.md` into your agent's skills directory, or rely on ResearchCraft which vendors it.
