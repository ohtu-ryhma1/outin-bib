import pytest
from services.input_validation import validate_reference


def test_validate_reference_success():
    fields = {
        "author": "Random Author",
        "title": "Example Article",
        "journaltitle": "Journal of Examples",
        "year/date": "2025"
    }
    validate_reference("article", "ref1", fields)

def test_validate_reference_missing_required():
    fields = {
        "author": "Random Author",
        "title": "Example Article"
    }
    with pytest.raises(ValueError, match="Required fields missing"):
        validate_reference("article", "ref2", fields)

def test_validate_reference_unknown_field():
    fields = {
        "author": "Random Author",
        "title": "Example Article",
        "journaltitle": "Journal of Examples",
        "year/date": "2025",
        "nonexistent": "unexpected"
    }
    with pytest.raises(ValueError, match="Unknown fields"):
        validate_reference("article", "ref3", fields)

def test_validate_reference_name_length():
    fields = {
        "author": "Random Author",
        "title": "Example Article",
        "journaltitle": "Journal of Examples",
        "year/date": "2025"
    }

    with pytest.raises(ValueError, match="Reference name must be 1-100 characters long"):
        validate_reference("article", "", fields)

    long_name = "x" * 101
    with pytest.raises(ValueError, match="Reference name must be 1-100 characters long"):
        validate_reference("article", long_name, fields)

def test_validate_reference_field_too_long():
    long_value = "x" * 501
    fields = {
        "author": "Random Author",
        "title": long_value,
        "journaltitle": "Journal of Examples",
        "year/date": "2025"
    }
    with pytest.raises(ValueError, match="cannot exceed 500 characters"):
        validate_reference("article", "ref5", fields)
