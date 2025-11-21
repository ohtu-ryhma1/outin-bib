import unittest
import sys
import os

# add src to sys.path to locate modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base import BaseTestCase
from models.reference import Reference
from models.field import Field

class TestReferenceWithField(BaseTestCase):
    def setUp(self):
        super().setUp()

        reference = Reference(type="book", name="test_name")
        field = Field(type="author", value="test_author")

        reference.fields.append(field)
        self.db.session.add(reference)
        self.db.session.commit()

        self.reference = reference

    def test_creation(self):
        self.assertIsNotNone(self.reference)

    def test_attribute_type(self):
        self.assertEqual(self.reference.type, "book")

    def test_attribute_name(self):
        self.assertEqual(self.reference.name, "test_name")

    def test_field_type(self):
        field = self.reference.fields[0]
        self.assertEqual(field.type, "author")

    def test_field_value(self):
        field = self.reference.fields[0]
        self.assertEqual(field.value, "test_author")


class TestReferenceWithoutField(BaseTestCase):
    def setUp(self):
        super().setUp()

        reference = Reference(type="book", name="test_name")

        self.db.session.add(reference)
        self.db.session.commit()

        self.reference = reference

    def test_creation(self):
        self.assertIsNotNone(self.reference)

    def test_fields_not_exist(self):
        self.assertEqual(self.reference.fields, [])
