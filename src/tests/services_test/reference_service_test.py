from src.repositories.reference_repository import ReferenceRepository
from src.services.reference_service import ReferenceService
from src.tests.base import BaseTestCase


class TestReferenceServiceWithReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        ref_data = {
            "type": "book",
            "name": "test_name",
            "fields": {
                "author": "test_author",
                "title": "test_title",
                "year/date": "2025",
            },
        }

        self.service.create(ref_data)

    def test_creation(self):
        self.assertIsNotNone(self.service)

    def test_references(self):
        reference = self.service.get_all().first()
        self.assertIsNotNone(reference)

    def test_reference_type(self):
        reference = self.service.get_all().first()
        self.assertEqual(reference.type, "book")

    def test_reference_field(self):
        reference = self.service.get_all().first()
        field = reference.fields[0]
        self.assertEqual(field.type, "author")


class TestReferenceServiceWithoutReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

    def test_creation(self):
        self.assertIsNotNone(self.service)

    def test_references(self):
        reference = self.service.get_all().first()
        self.assertIsNone(reference)


class TestReferenceServiceWithIncorrectInput(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        self.ref_data = {
            "type": "book",
            "name": "test_name",
            "fields": {
                "author": "test_author",
                "title": "test_title",
                "year/date": "2025",
            },
        }

    def test_missing_name(self):
        self.ref_data["name"] = ""
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_missing_required_field(self):
        self.ref_data["fields"] = {}
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_missing_year_date(self):
        self.ref_data["fields"]["year/date"] = ""
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_too_long_name(self):
        self.ref_data["name"] = "test_name" * 100
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_unknown_field(self):
        self.ref_data["fields"]["unexpected"] = "value"
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_field_too_long(self):
        self.ref_data["fields"]["author"] = "x" * 501
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_valid_reference_creation(self):
        result = self.service.create(self.ref_data)
        self.assertIsNotNone(result)
        self.assertEqual(result.name, self.ref_data["name"])
