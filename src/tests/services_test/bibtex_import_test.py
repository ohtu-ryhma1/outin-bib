import unittest

from src.services.bibtex_import import normalize_field_name


class TestNormalizeFieldName(unittest.TestCase):
    def test_journal_to_journaltitle(self):
        self.assertEqual(normalize_field_name("journal"), "journaltitle")

    def test_year_to_year_date(self):
        self.assertEqual(normalize_field_name("year"), "year/date")

    def test_date_to_year_date(self):
        self.assertEqual(normalize_field_name("date"), "year/date")

    def test_unchanged_field(self):
        self.assertEqual(normalize_field_name("author"), "author")
        self.assertEqual(normalize_field_name("title"), "title")

    def test_case_insensitive(self):
        self.assertEqual(normalize_field_name("JOURNAL"), "journaltitle")
        self.assertEqual(normalize_field_name("Year"), "year/date")
