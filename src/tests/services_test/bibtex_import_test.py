import unittest

from src.services.bibtex_import import import_bibtex_text, normalize_field_name
from src.tests.base import BaseTestCase


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


class TestImportBibtexWithGenericFields(BaseTestCase):
    def test_import_with_abstract_field(self):
        """Test that importing with abstract (a generic field) does not fail."""
        bibtex_text = """
        @article{testkey,
         author = "John Doe",
         title = "Test Article",
         journaltitle = "Test Journal",
         year = 2024,
         abstract = "This is an abstract for the article.",
        }"""
        success_count, errors = import_bibtex_text(bibtex_text)
        self.assertEqual(success_count, 1)
        self.assertEqual(len(errors), 0)

    def test_import_with_multiple_generic_fields(self):
        """Test that importing with multiple generic fields works."""
        bibtex_text = """
        @book{testbook,
         author = "Jane Smith",
         title = "Test Book",
         year = 2023,
         keywords = "testing, python",
         annotation = "A note about this book",
         shorttitle = "Test",
         label = "smith2023",
        }"""
        success_count, errors = import_bibtex_text(bibtex_text)
        self.assertEqual(success_count, 1)
        self.assertEqual(len(errors), 0)


class TestImportBibtexWithCrossref(BaseTestCase):
    def test_import_allows_entry_with_crossref(self):
        """Test that entry with crossref imports successfully even without required fields."""
        bibtex_text = """
        @incollection{westfahl:space,
         author = "Gary Westfahl",
         title = "The True Frontier",
         crossref = "westfahl:frontier",
        }

        @collection{westfahl:frontier,
         editor = "Editor Person",
         title = "Frontier Studies",
         year = 1999,
        }"""
        success_count, errors = import_bibtex_text(bibtex_text)
        self.assertEqual(success_count, 2)
        self.assertEqual(len(errors), 0)

    def test_import_fails_if_entry_without_crossref_missing_required_fields(self):
        """Test that entry without crossref fails if missing required fields."""
        bibtex_text = """
        @incollection{item1,
         title = "Missing author and other required fields",
        }"""
        success_count, errors = import_bibtex_text(bibtex_text)
        self.assertEqual(success_count, 0)
        self.assertEqual(len(errors), 1)
        self.assertIn("Required fields missing", errors[0])

    def test_import_crossref_entry_with_minimal_fields(self):
        """Test that crossref entry with only crossref field imports successfully."""
        bibtex_text = """
        @inbook{child:entry,
         crossref = "parent:entry",
        }

        @book{parent:entry,
         author = "Parent Author",
         title = "Parent Book",
         year = 2020,
        }"""
        success_count, errors = import_bibtex_text(bibtex_text)
        self.assertEqual(success_count, 2)
        self.assertEqual(len(errors), 0)
