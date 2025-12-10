import unittest

from src.services.bibtex_exporter import references_to_bibtex

"""
self.assertEqual(
            {            
                "ENTRYTYPE": "",
                "ID": "",
            }, result )
"""

class MockField:
    def __init__(self, field_type, value):
        self.type = field_type
        self.value = value


class MockReference:
    def __init__(self, ref_type, key, fields):
        self.type = ref_type
        self.key = key
        self.fields = [MockField(k, v) for k, v in fields.items()]


class TestReferencesToBibtex(unittest.TestCase):
    def test_multiple_references(self):
        refs = [
            MockReference(
                "article",
                "key1",
                {
                    "author": "Author One",
                    "title": "Title One",
                    "journaltitle": "Journal",
                    "year/date": "2020",
                },
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
                "article",
                "single",
                {
                    "author": "Solo Author",
                    "title": "Solo",
                    "journaltitle": "Journal",
                    "year/date": "2024",
                },
            )
        ]

        result = references_to_bibtex(refs)

        self.assertIn("@article{single,", result)
        # Should not have double newline separator when single entry
        self.assertEqual(result.count("\n\n"), 0)
