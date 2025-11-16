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
            Field("title", "Book Name"),
            Field("author", "Author Name"),
            Field("year", "2025")
        ]

        ref = Reference(reference_type="book", name="TestBook", fields=fields)

        self.assertTrue(all(isinstance(f, Field) for f in ref.fields))

        self.assertEqual(ref.get_field("title").value, "Book Name")
        self.assertEqual(ref.get_field("author").value, "Author Name")
        self.assertEqual(ref.get_field("year").value, "2025")
        self.assertIsNone(ref.get_field("nonexistent_field"))

    def test_get_field_url(self):
        fields = [
            Field("title", "Article Name"),
            Field("author", "Author Name"),
            Field("year", "2025"),
            Field("url", "https://www.example.fi")
        ]

        ref = Reference(reference_type="website", name="ExampleSite", fields=fields)

        self.assertTrue(all(isinstance(f, Field) for f in ref.fields))
        self.assertEqual(ref.get_field("title").value, "Article Name")
        self.assertEqual(ref.get_field("author").value, "Author Name")
        self.assertEqual(ref.get_field("year").value, "2025")
        self.assertEqual(ref.get_field("url").value, "https://www.example.fi")
        self.assertIsNone(ref.get_field("imaginary_field"))

if __name__ == "__main__":
    unittest.main()
