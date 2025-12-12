import unittest

from src.scripts.bibtex_types import generic_fields, types
from src.services.reference_types import (
    get_all_field_types,
    get_reference_fields,
    get_reference_types,
)


class TestReferenceTypes(unittest.TestCase):
    def test_get_reference_types_matches_keys(self):
        self.assertEqual(get_reference_types(), set(types.keys()))

    def test_get_reference_fields_valid(self):
        for ref_type in types:
            required, optional = get_reference_fields(ref_type)
            self.assertIsInstance(required, list)
            self.assertIsInstance(optional, list)
            for f in required:
                self.assertIsInstance(f, str)
            for f in optional:
                self.assertIsInstance(f, str)

    def test_get_reference_fields_invalid(self):
        with self.assertRaises(ValueError) as context:
            get_reference_fields("nonexistent_type")
            self.assertIn("Invalid reference type", str(context.exception))

    def test_get_reference_fields_article(self):
        expected_required = ["author", "title", "journaltitle", "year/date"]
        type_specific_optional = [
            "translator",
            "annotator",
            "commentator",
            "subtitle",
            "titleaddon",
            "editor",
            "editora",
            "editorb",
            "editorc",
            "journalsubtitle",
            "journaltitleaddon",
            "issuetitle",
            "issuesubtitle",
            "issuetitleaddon",
            "language",
            "origlanguage",
            "series",
            "volume",
            "number",
            "eid",
            "issue",
            "month",
            "pages",
            "version",
            "note",
            "issn",
            "addendum",
            "pubstate",
            "doi",
            "eprint",
            "eprintclass",
            "eprinttype",
            "url",
            "urldate",
        ]

        required, optional = get_reference_fields("article")
        self.assertEqual(required, expected_required)

        # All type-specific optional fields should be present
        for field in type_specific_optional:
            self.assertIn(field, optional)

        # All generic fields (except those in required) should be in optional
        for field in generic_fields:
            if field not in expected_required:
                self.assertIn(field, optional)

        # No duplicates in optional
        self.assertEqual(len(optional), len(set(optional)))

        # No required fields in optional
        for field in expected_required:
            self.assertNotIn(field, optional)

    def test_generic_fields_included_in_all_types(self):
        """Test that generic fields are available as optional for all types."""
        for ref_type in types:
            required, optional = get_reference_fields(ref_type)
            required_set = set(required)
            optional_set = set(optional)

            # All generic fields should be in optional (unless they're required)
            for field in generic_fields:
                if field not in required_set:
                    self.assertIn(
                        field,
                        optional_set,
                        f"Generic field '{field}' missing from {ref_type} optional fields",
                    )

            # No duplicates in optional
            self.assertEqual(
                len(optional), len(optional_set), f"Duplicates found in {ref_type}"
            )

            # No required fields in optional
            for field in required:
                self.assertNotIn(
                    field,
                    optional_set,
                    f"Required field '{field}' found in optional for {ref_type}",
                )

    def test_get_all_field_types_contains_common_fields(self):
        fields = get_all_field_types()
        assert isinstance(fields, set)
        assert "author" in fields
        assert "title" in fields
