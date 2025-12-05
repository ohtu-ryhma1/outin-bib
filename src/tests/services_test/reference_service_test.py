from src.repositories.reference_repository import ReferenceRepository
from src.services.reference_service import ReferenceService
from src.tests.base import BaseTestCase


class TestReferenceServiceWithReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        self.ref_data = {
            "type": "book",
            "key": "test_key",
            "fields": {
                "author": "test_author",
                "title": "test_title",
                "year/date": "2025",
            },
        }

        self.service.create(self.ref_data)

    def test_creation(self):
        self.assertIsNotNone(self.service)

    def test_references(self):
        reference = self.service.get()
        self.assertIsNotNone(reference)

    def test_reference_type(self):
        reference = self.service.get()
        self.assertEqual(reference.type, "book")

    def test_reference_field(self):
        reference = self.service.get()
        field = reference.fields[0]
        self.assertEqual(field.type, "author")

    def test_update_reference_key(self):
        ref_id = self.service.get().id
        self.ref_data["key"] = "new_test_key"
        self.service.update(ref_id, self.ref_data)

        ref_key = self.service.get(ref_id=ref_id).key
        self.assertEqual(ref_key, "new_test_key")


class TestReferenceServiceWithoutReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

    def test_creation(self):
        self.assertIsNotNone(self.service)

    def test_references(self):
        with self.assertRaises(LookupError):
            self.service.get()


class TestReferenceServiceWithIncorrectInput(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        self.ref_data = {
            "type": "book",
            "key": "test_key",
            "fields": {
                "author": "test_author",
                "title": "test_title",
                "year/date": "2025",
            },
        }

    def test_missing_key(self):
        self.ref_data["key"] = ""
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

    def test_too_long_key(self):
        self.ref_data["key"] = "test_key" * 100
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_unknown_field(self):
        self.ref_data["fields"]["unexpected"] = "value"
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_field_too_long(self):
        self.ref_data["fields"]["author"] = "x" * 1501
        with self.assertRaises(ValueError):
            self.service.create(self.ref_data)

    def test_valid_reference_creation(self):
        result = self.service.create(self.ref_data)
        self.assertIsNotNone(result)
        self.assertEqual(result.key, self.ref_data["key"])


class TestReferenceServiceUpdateWithIncorrectInput(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        self.ref_data = {
            "type": "book",
            "key": "test_key",
            "fields": {
                "author": "test_author",
                "title": "test_title",
                "year/date": "2025",
            },
        }

        self.service.create(self.ref_data)

    def test_update_incorrect_reference_key(self):
        ref_id = self.service.get().id
        self.ref_data["key"] = "new_test_key" * 50
        with self.assertRaises(ValueError):
            self.service.update(ref_id, self.ref_data)

    def test_update_missing_required_field(self):
        ref_id = self.service.get().id
        self.ref_data["fields"].pop("author")
        with self.assertRaises(ValueError):
            self.service.update(ref_id, self.ref_data)


class TestReferenceServiceMetadataMethods(BaseTestCase):
    def setUp(self):
        super().setUp()
        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)
        self.ref_data = {
            "type": "book",
            "key": "meta_test_key",
            "fields": {
                "author": "author_meta",
                "title": "title_meta",
                "year/date": "2025",
            },
        }
        self.service.create(self.ref_data)

    def test_get_all_meta_returns_references_with_counts(self):
        refs = self.service.get_all_meta()
        self.assertTrue(len(refs) >= 1)
        ref = refs[0]
        self.assertGreaterEqual(ref.required_count, 1)
        self.assertGreaterEqual(ref.optional_count, 0)

    def test_get_meta_returns_single_reference_with_counts(self):
        ref_id = self.service.get().id
        ref = self.service.get_meta(ref_id)
        self.assertIsNotNone(ref)
        self.assertTrue(hasattr(ref, "required_count"))
        self.assertTrue(hasattr(ref, "optional_count"))

    def test_delete_all_removes_all_references(self):
        self.service.delete_all()
        refs = self.service.get_all()
        self.assertEqual(len(refs), 0)
