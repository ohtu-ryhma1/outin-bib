import unittest
from unittest.mock import MagicMock

from src.services.bibtex_exporter import reference_to_bibtex, references_to_bibtex


class MockField:
    def __init__(self, field_type, value):
        self.type = field_type
        self.value = value


class MockReference:
    def __init__(self, ref_type, name, fields):
        self.type = ref_type
        self.name = name
        self.fields = [MockField(k, v) for k, v in fields.items()]


class TestReferenceToBibtex(unittest.TestCase):
    def test_simple_article(self):
        ref = MockReference(
            "article",
            "testkey",
            {
                "author": "John Doe",
                "title": "Test Article",
                "journaltitle": "Test Journal",
                "year/date": "2024",
            },
        )

        result = reference_to_bibtex(ref)

        self.assertIn("@article{testkey,", result)
        self.assertIn("author = {John Doe},", result)
        self.assertIn("title = {Test Article},", result)
        self.assertIn("journaltitle = {Test Journal},", result)
        self.assertIn("year/date = {2024},", result)
        self.assertTrue(result.endswith("}"))

    def test_book_reference(self):
        ref = MockReference(
            "book", "bookkey", {"author": "Jane Smith", "title": "A Book", "year/date": "2023"}
        )

        result = reference_to_bibtex(ref)

        self.assertIn("@book{bookkey,", result)
        self.assertIn("author = {Jane Smith},", result)

    def test_empty_fields(self):
        ref = MockReference("misc", "emptykey", {})

        result = reference_to_bibtex(ref)

        self.assertEqual(result, "@misc{emptykey,\n}")


class TestReferencesToBibtex(unittest.TestCase):
    def test_multiple_references(self):
        refs = [
            MockReference(
                "article",
                "key1",
                {"author": "Author One", "title": "Title One", "journaltitle": "Journal", "year/date": "2020"},
            ),
            MockReference(
                "book",
                "key2",
                {"author": "Author Two", "title": "Title Two", "year/date": "2021"},
            ),
        ]

        result = references_to_bibtex(refs)

        self.assertIn("@article{key1,", result)
        self.assertIn("@book{key2,", result)
        # Entries should be separated by double newlines
        self.assertIn("\n\n", result)

    def test_empty_list(self):
        result = references_to_bibtex([])
        self.assertEqual(result, "")

    def test_single_reference(self):
        refs = [
            MockReference(
                "article", "single", {"author": "Solo Author", "title": "Solo", "journaltitle": "Journal", "year/date": "2024"}
            )
        ]

        result = references_to_bibtex(refs)

        self.assertIn("@article{single,", result)
        # Should not have double newline separator when single entry
        self.assertEqual(result.count("\n\n"), 0)
