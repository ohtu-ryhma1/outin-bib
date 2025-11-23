import pytest

from scripts.bibtex_types import types
from services.reference_types import get_reference_fields, get_reference_types


def test_get_reference_types_matches_keys():
    assert get_reference_types() == set(types.keys())

def test_get_reference_fields_valid():
    for ref_type in types:
        required, optional = get_reference_fields(ref_type)
        assert isinstance(required, list)
        assert isinstance(optional, list)
        assert all(isinstance(f, str) for f in required)
        assert all(isinstance(f, str) for f in optional)

def test_get_reference_fields_invalid():
    with pytest.raises(ValueError) as excinfo:
        get_reference_fields("nonexistent_type")
    assert "Invalid reference type" in str(excinfo.value)

def test_get_reference_fields_article():
    expected_required = ["author", "title", "journaltitle", "year/date"]
    expected_optional = [
        "translator", "annotator", "commentator", "subtitle", "titleaddon",
        "editor", "editora", "editorb", "editorc", "journalsubtitle",
        "journaltitleaddon", "issuetitle", "issuesubtitle", "issuetitleaddon",
        "language", "origlanguage", "series", "volume", "number", "eid", "issue",
        "month", "pages", "version", "note", "issn", "addendum", "pubstate", "doi",
        "eprint", "eprintclass", "eprinttype", "url", "urldate"
    ]

    required, optional = get_reference_fields("article")
    assert required == expected_required
    assert optional == expected_optional
