# Ingest

## One paper, one record

Pass the DOI **with** the PDF so metadata and chunks share an id:

```bash
papermemory ingest paper.pdf --doi 10.1371/journal.pone.0130140 --json
```

That sets `verified=1`, stores the DOI, and indexes it. A later markdown conversion attaches to the same row:

```bash
papermemory ingest paper.md --pdf-path paper.pdf --json
```

`--title` keeps a canonical title when the PDF header is an arXiv banner.

## Sources

| Input | Command |
| --- | --- |
| PDF | `ingest PATH` (`pypdf` required) |
| PDF + DOI | `ingest PATH --doi DOI` |
| Markdown / TeX | `ingest PATH` |
| Markdown onto a PDF | `ingest PATH --pdf-path paper.pdf` |
| BibTeX | `ingest refs.bib` |
| Manuscript tree | `ingest DIR --kind manuscript --project SLUG` |
| arXiv | `ingest --arxiv ID` |
| Crossref DOI | `ingest --doi DOI` |

`--doi` without a path still does a Crossref-only lookup. With a path, Crossref (if it succeeds) runs first, then the file merges onto that paper.

## Search

Hybrid FTS over titles, authors, venue, DOI, arXiv id, `pdf_path`, abstracts, chunks, claims, and notes. Empty `cite` means do not invent a reference — see [[Citations]].
