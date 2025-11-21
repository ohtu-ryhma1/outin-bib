import unittest
import sys
import os

# add src to sys.path to locate modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from base import BaseTestCase
from repositories.reference_repository import ReferenceRepository
from services.reference_service import ReferenceService


class TestReferenceRepositoryWithReference(BaseTestCase):
    def setUp(self):
        super().setUp()

        repo = ReferenceRepository(self.db)
        self.service = ReferenceService(repo)

        ref_data = {
            "type": "book",
            "name": "test_name",
            "fields": {"author": "test_author"}
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
