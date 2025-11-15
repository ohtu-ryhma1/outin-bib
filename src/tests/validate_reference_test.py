"""Unittests for Reference and Field objects"""
import unittest
import sys
import os
from entities.reference import Reference
from entities.field import Field

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestReference(unittest.TestCase):
    def test_get_field_book(self):
        fields = [
            Field(1, "title", "Book Name"),
            Field(2, "author", "Author Name"),
            Field(3, "year", "2025")
        ]

        ref = Reference(entry_id=1, type_name="book", fields=fields)

        self.assertTrue(all(isinstance(f, Field) for f in ref.fields))
        self.assertEqual(ref.get("title"), "Book Name")
        self.assertEqual(ref.get("author"), "Author Name")
        self.assertEqual(ref.get("year"), "2025")
        self.assertIsNone(ref.get("nonexistent_field"))

    def test_get_field_url(self):
        fields = [
            Field(1, "title", "Article Name"),
            Field(2, "author", "Author Name"),
            Field(3, "year", "2025"),
            Field(4, "url", "https://www.example.fi")
        ]

        ref = Reference(entry_id=2, type_name="website", fields=fields)

        self.assertTrue(all(isinstance(f, Field) for f in ref.fields))
        self.assertEqual(ref.get("title"), "Article Name")
        self.assertEqual(ref.get("author"), "Author Name")
        self.assertEqual(ref.get("year"), "2025")
        self.assertEqual(ref.get("url"), "https://www.example.fi")
        self.assertIsNone(ref.get("imaginary_field"))

if __name__ == "__main__":
    unittest.main()
