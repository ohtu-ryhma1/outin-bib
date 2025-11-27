import unittest

from src.scripts.bibtex_types import types
from src.services.reference_types import get_reference_fields, get_reference_types


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
        expected_optional = [
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
        self.assertEqual(optional, expected_optional)
