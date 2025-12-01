from src.repositories.reference_repository import ReferenceRepository
from src.tests.base import BaseTestCase


class TestReferenceRepositoryWithReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.repo = ReferenceRepository(self.db)

        self.ref_data = {
            "type": "book",
            "name": "test_name",
            "fields": {"author": "test_author"},
        }

        self.repo.create(self.ref_data)

    def test_creation(self):
        self.assertIsNotNone(self.repo)

    def test_references(self):
        reference = self.repo.get()
        self.assertIsNotNone(reference)

    def test_reference_type(self):
        reference = self.repo.get()
        self.assertEqual(reference.type, "book")

    def test_reference_field(self):
        reference = self.repo.get()
        field = reference.fields[0]
        self.assertEqual(field.type, "author")

    def test_update_reference_name(self):
        ref_id = self.repo.get().id
        self.ref_data["name"] = "new_test_name"
        self.repo.update(ref_id, self.ref_data)

        ref_name = self.repo.get(ref_id=ref_id).name
        self.assertEqual(ref_name, "new_test_name")

    def test_update_reference_type(self):
        ref_id = self.repo.get().id
        self.ref_data["type"] = "article"
        self.repo.update(ref_id, self.ref_data)

        ref_type = self.repo.get(ref_id=ref_id).type
        self.assertEqual(ref_type, "article")

    def test_update_reference_field(self):
        ref_id = self.repo.get().id
        self.ref_data["fields"]["year"] = "2025"
        self.repo.update(ref_id, self.ref_data)

        fields = self.repo.get(ref_id=ref_id).fields
        field = next((f for f in fields if f.type == "year"), None)
        year = field.value if field else None
        self.assertEqual(year, "2025")


class TestReferenceRepositoryWithoutReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.repo = ReferenceRepository(self.db)

    def test_creation(self):
        self.assertIsNotNone(self.repo)

    def test_references(self):
        with self.assertRaises(LookupError):
            self.repo.get()
