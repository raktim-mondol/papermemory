"""Citation-key generation.

The default policy matches the Academic Harness ``citation`` tool so both
sides produce the same key for the same record:
``{family}{year}{first significant title word}``, ASCII, lower case, never
starting with a digit. Uniqueness and stability are handled by
``library_store`` (library-wide unique keys, letter suffixes, frozen keys).
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

_STOP = {"a", "an", "the", "on", "of", "for", "and", "in", "to", "with", "from"}
_USABLE_SOURCE_KEY = re.compile(r"^[A-Za-z][A-Za-z0-9_:.\-/+]*$")


def _slug_word(value: str) -> str:
    text = unicodedata.normalize("NFKD", value or "")
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    return re.sub(r"[^A-Za-z0-9]+", "", text).lower()


def make_key(csl: dict[str, Any]) -> str:
    authors = csl.get("author") or csl.get("editor") or []
    first = authors[0] if authors else {}
    family = _slug_word(first.get("family") or first.get("literal") or "") or "anon"
    parts = (csl.get("issued") or {}).get("date-parts") or []
    year = str(parts[0][0]) if parts and parts[0] else "nd"
    words = [w for w in (_slug_word(t) for t in str(csl.get("title") or "untitled").split()) if w]
    word = next((w for w in words if len(w) > 2 and w not in _STOP), words[0] if words else "untitled")
    key = f"{family}{year}{word}"[:48]
    return f"ref{key}" if key[:1].isdigit() else key


def usable_source_key(key: str | None) -> bool:
    """A key from a source file is kept as written when it is a valid cite key.

    Purely numeric ids (common in publisher RIS exports) are not citation keys.
    """
    return bool(key) and bool(_USABLE_SOURCE_KEY.match(key))
