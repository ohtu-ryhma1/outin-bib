from src.repositories.reference_repository import ReferenceRepository
from src.tests.base import BaseTestCase


class TestReferenceRepositoryWithReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.repo = ReferenceRepository(self.db)

        ref_data = {
            "type": "book",
            "name": "test_name",
            "fields": {"author": "test_author"},
        }

        self.repo.create(ref_data)

    def test_creation(self):
        self.assertIsNotNone(self.repo)

    def test_references(self):
        reference = self.repo.get_all().first()
        self.assertIsNotNone(reference)

    def test_reference_type(self):
        reference = self.repo.get_all().first()
        self.assertEqual(reference.type, "book")

    def test_reference_field(self):
        reference = self.repo.get_all().first()
        field = reference.fields[0]
        self.assertEqual(field.type, "author")


class TestReferenceRepositoryWithoutReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        self.repo = ReferenceRepository(self.db)

    def test_creation(self):
        self.assertIsNotNone(self.repo)

    def test_references(self):
        reference = self.repo.get_all().first()
        self.assertIsNone(reference)
