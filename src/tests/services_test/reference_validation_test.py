import unittest

from src.services.reference_validation import (
    ErrorCode,
    ValidationException,
    validate_reference,
)


class TestValidateReference(unittest.TestCase):
    def setUp(self):
        self.valid_fields = {
            "author": "test_author",
            "title": "test_title",
            "journaltitle": "test_journaltitle",
            "year/date": "2025",
        }

        self.ref_data = {
            "type": "article",
            "key": "test_key",
            "fields": self.valid_fields,
        }

    def test_valid_date_succeeds(self):
        validate_reference(self.ref_data)

    def test_missing_required_field_fails(self):
        self.valid_fields.pop("year/date")
        with self.assertRaises(ValidationException) as context:
            validate_reference(self.ref_data)
        self.assertIs(context.exception.code, ErrorCode.REQUIRED_FIELD_MISSING)

    def test_unknown_field_fails(self):
        self.valid_fields["invalid_field"] = "value"
        with self.assertRaises(ValidationException) as context:
            validate_reference(self.ref_data)
        self.assertIs(context.exception.code, ErrorCode.UNKNOWN_FIELD_PRESENT)

    def test_key_too_short_fails(self):
        self.ref_data["key"] = ""
        with self.assertRaises(ValidationException) as context:
            validate_reference(self.ref_data)
        self.assertIs(context.exception.code, ErrorCode.KEY_LENGTH_INVALID)

    def test_key_too_long_fails(self):
        self.ref_data["key"] = "x" * 101
        with self.assertRaises(ValidationException) as context:
            validate_reference(self.ref_data)
        self.assertIs(context.exception.code, ErrorCode.KEY_LENGTH_INVALID)

    def test_field_too_long_fails(self):
        self.valid_fields["title"] = "x" * 1501
        with self.assertRaises(ValidationException) as context:
            validate_reference(self.ref_data)
        self.assertIs(context.exception.code, ErrorCode.FIELD_LENGTH_INVALID)
