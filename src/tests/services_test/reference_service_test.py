import unittest
from unittest.mock import MagicMock, Mock, patch

from src.repositories.reference_repository import ReferenceRepository
from src.services.reference_service import ReferenceService
from src.services.reference_validation import ValidationException


def make_ref_data(
    key="test_key",
    author="test_author",
    title="test_title",
    year="2025",
    extra_fields=None,
):
    fields = {"author": author, "title": title, "year/date": year}
    fields.update(extra_fields or {})
    return {"type": "book", "key": key, "fields": fields}


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = MagicMock(spec=ReferenceRepository)
        self.service = ReferenceService(self.repo)


class TestGet(BaseTestCase):
    def test_calls_repo_get(self):
        self.service.get()
        self.repo.get.assert_called_once_with(None)

    def test_calls_repo_get_with_id(self):
        self.service.get(42)
        self.repo.get.assert_called_once_with(42)

    def test_repo_get_exception_propagates(self):
        self.repo.get.side_effect = LookupError
        with self.assertRaises(LookupError):
            self.service.get()


class TestGetMeta(BaseTestCase):
    def test_calls_repo_get(self):
        self.repo.get.return_value = Mock(type="book", fields=[])
        self.service.get_meta()
        self.repo.get.assert_called_once_with(None)

    def test_calls_repo_get_with_id(self):
        self.repo.get.return_value = Mock(type="book", fields=[])
        self.service.get_meta(42)
        self.repo.get.assert_called_once_with(42)

    def test_repo_get_exception_propagates(self):
        self.repo.get.side_effect = LookupError
        with self.assertRaises(LookupError):
            self.service.get_meta()

    def test_returns_ref_with_meta(self):
        with patch(
            "src.services.reference_service.get_reference_fields",
            return_value=(["r1", "r2"], ["o1"]),
        ):
            f1 = Mock(type="r1")
            f2 = Mock(type="r2")
            f3 = Mock(type="o1")
            f4 = Mock(type="other")

            ref = Mock(type="any", fields=[f1, f3, f4, f2])

            self.repo.get.return_value = ref

            result = self.service.get_meta()

            self.assertEqual(result.required, ["r1", "r2"])
            self.assertEqual(result.optional, ["o1"])
            self.assertEqual(result.required_count, 2)
            self.assertEqual(result.optional_count, 1)


class TestGetAll(BaseTestCase):
    def test_calls_repo_get_all(self):
        self.service.get_all()
        self.repo.get_all.assert_called_once_with()


class TestGetAllMeta(BaseTestCase):
    def test_calls_repo_get_all_with_args(self):
        self.service.get_all_meta(
            key="abc", types=["book", "article"], field_filters=[("author", "test")]
        )
        self.repo.get_all.assert_called_once_with(
            "abc", ["book", "article"], [("author", "test")]
        )

    def test_returns_refs_with_meta(self):
        with patch(
            "src.services.reference_service.get_reference_fields",
            return_value=(["r1", "r2"], ["o1"]),
        ):
            f1 = Mock(type="r1")
            f2 = Mock(type="r2")
            f3 = Mock(type="o1")
            f4 = Mock(type="other")

            ref1 = Mock(type="any", fields=[f1, f3, f4])
            ref2 = Mock(type="any", fields=[f2])

            self.repo.get_all.return_value = [ref1, ref2]

            refs = self.service.get_all_meta()

            self.assertEqual(len(refs), 2)

            self.assertEqual(refs[0].required, ["r1", "r2"])
            self.assertEqual(refs[0].optional, ["o1"])
            self.assertEqual(refs[0].required_count, 1)
            self.assertEqual(refs[0].optional_count, 1)

            self.assertEqual(refs[1].required_count, 1)
            self.assertEqual(refs[1].optional_count, 0)


class TestCreate(BaseTestCase):
    def test_calls_validate_reference(self):
        ref_data = make_ref_data()
        with patch(
            "src.services.reference_service.validate_reference"
        ) as mock_validate:
            self.service.create(ref_data)
            mock_validate.assert_called_once_with(ref_data)

    def test_calls_repo_create(self):
        ref_data = make_ref_data()
        with patch("src.services.reference_service.validate_reference"):
            self.service.create(ref_data)
            self.repo.create.assert_called_once_with(ref_data)

    def test_repo_create_exception_propagates(self):
        ref_data = make_ref_data()
        with patch("src.services.reference_service.validate_reference"):
            self.repo.create.side_effect = Exception("DB error")
            with self.assertRaises(Exception) as context:
                self.service.create(ref_data)
            self.assertEqual(str(context.exception), "DB error")

    def test_validation_exception_propagates(self):
        ref_data = make_ref_data()
        with patch(
            "src.services.reference_service.validate_reference"
        ) as mock_validate:
            mock_validate.side_effect = ValidationException
            with self.assertRaises(ValidationException):
                self.service.create(ref_data)


class TestUpdate(BaseTestCase):
    def test_calls_validate_reference(self):
        ref_data = make_ref_data()
        with patch(
            "src.services.reference_service.validate_reference"
        ) as mock_validate:
            self.service.update(1, ref_data)
            mock_validate.assert_called_once_with(ref_data)

    def test_calls_repo_update(self):
        ref_data = make_ref_data()
        with patch("src.services.reference_service.validate_reference"):
            self.service.update(1, ref_data)
            self.repo.update.assert_called_once_with(1, ref_data)

    def test_repo_update_exception_propagates(self):
        ref_data = make_ref_data()
        with patch("src.services.reference_service.validate_reference"):
            self.repo.update.side_effect = ValidationException
            with self.assertRaises(ValidationException):
                self.service.update(1, ref_data)


class TestDeleteAll(BaseTestCase):
    def test_calls_repo_delete_all(self):
        self.service.delete_all()
        self.repo.delete_all.assert_called_once()
