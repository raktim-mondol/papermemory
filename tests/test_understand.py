from papermemory.understand import extract_claims, split_sections, understand_text


TEXT = """
Title of a Fake Paper

Abstract
We propose a hybrid CNN-ViT method for spoil classification. Results reach 95.1% accuracy.

1. Introduction
Coal spoil dumps fail when shear strength is misestimated. This paper presents SCANDY.

2. Methods
We use attention-based multiple instance learning on pile-level images.

3. Results
The model outperforms a ResNet-50 baseline on QLD1.

4. Limitations
The dataset is limited to two Queensland sites.

References
Simmons 2004.
"""


def test_split_and_claims():
    sections = split_sections(TEXT)
    names = [s["section"] for s in sections]
    assert "abstract" in names
    assert "methods" in names
    assert "limitations" in names
    claims = extract_claims(sections)
    assert claims
    types = {c["claim_type"] for c in claims}
    assert "method" in types or "finding" in types
    summary = understand_text(TEXT)
    assert summary["chunks"]
    assert summary["abstract"]
