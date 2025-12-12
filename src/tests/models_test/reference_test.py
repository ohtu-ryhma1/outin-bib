from src.models.field import Field
from src.models.reference import Reference
from src.tests.base import BaseTestCase


class TestReferenceWithField(BaseTestCase):
    def setUp(self):
        super().setUp()

        reference = Reference(type="book", key="test_key")
        field = Field(type="author", value="test_author")

        reference.fields.append(field)
        self.db.session.add(reference)
        self.db.session.commit()

        self.reference = reference

    def test_creation(self):
        self.assertIsNotNone(self.reference)

    def test_attribute_type(self):
        self.assertEqual(self.reference.type, "book")

    def test_attribute_key(self):
        self.assertEqual(self.reference.key, "test_key")

    def test_field_type(self):
        field = self.reference.fields[0]
        self.assertEqual(field.type, "author")

    def test_field_value(self):
        field = self.reference.fields[0]
        self.assertEqual(field.value, "test_author")

    def test_reference_repr(self):
        string = "Reference(id=1, type='book', key='test_key')"
        self.assertEqual(repr(self.reference), string)

    def test_field_repr(self):
        field = self.reference.fields[0]
        string = "Field(id=1, type='author', value='test_author')"
        self.assertEqual(repr(field), string)


class TestReferenceWithoutField(BaseTestCase):
    def setUp(self):
        super().setUp()

        reference = Reference(type="book", key="test_key")

        self.db.session.add(reference)
        self.db.session.commit()

        self.reference = reference

    def test_creation(self):
        self.assertIsNotNone(self.reference)

    def test_fields_not_exist(self):
        self.assertEqual(self.reference.fields, [])

    def test_reference_repr(self):
        string = "Reference(id=1, type='book', key='test_key')"
        self.assertEqual(repr(self.reference), string)
