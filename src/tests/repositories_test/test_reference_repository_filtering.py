from src.repositories.reference_repository import ReferenceRepository
from src.tests.base import BaseTestCase


class TestReferenceRepositoryFiltering(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.repo = ReferenceRepository(self.db)

        self.repo.create(
            {
                "type": "book",
                "key": "first",
                "fields": {"author": "John", "title": "Book A"},
            }
        )
        self.repo.create(
            {
                "type": "article",
                "key": "second",
                "fields": {"author": "Jane", "title": "Science Today"},
            }
        )

    def test_filter_by_key(self):
        refs = self.repo.get_all(key="fir")
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].key, "first")

    def test_filter_by_type(self):
        refs = self.repo.get_all(types=["article"])
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].type, "article")

    def test_filter_by_field(self):
        refs = self.repo.get_all(field_filters=[("author", "Jane")])
        self.assertEqual(len(refs), 1)
        self.assertEqual(refs[0].fields[0].value, "Jane")
