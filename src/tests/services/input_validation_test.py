import unittest

from services.input_validation import validate_reference


class TestValidateReference(unittest.TestCase):
    def setUp(self):
        self.valid_fields = {
            "author": "Random Author",
            "title": "Example Article",
            "journaltitle": "Journal of Examples",
            "year/date": "2025"
        }
        self.ref_data = {
            "type": "article",
            "name": "ref1",
            "fields": self.valid_fields
        }

    def test_validate_reference_success(self):
        validate_reference(self.ref_data)

    def test_validate_reference_missing_required(self):
        self.valid_fields.pop("year/date")
        with self.assertRaises(ValueError) as context:
            validate_reference(self.ref_data)
        self.assertIn("Required fields missing", str(context.exception))

    def test_validate_reference_unknown_field(self):
        self.valid_fields["nonexistent"] = "unknown"
        with self.assertRaises(ValueError) as context:
            validate_reference(self.ref_data)
        self.assertIn("Unknown fields", str(context.exception))

    def test_validate_reference_name_min_length(self):
        self.ref_data["name"] = ""
        with self.assertRaises(ValueError) as context:
            validate_reference(self.ref_data)
        self.assertIn("Reference name must be 1-100 characters long", str(context.exception))

    def test_validate_reference_name_max_length(self):
        self.ref_data["name"] = "x" * 101
        with self.assertRaises(ValueError) as context:
            validate_reference(self.ref_data)
        self.assertIn("Reference name must be 1-100 characters long", str(context.exception))

    def test_validate_reference_field_too_long(self):
        self.valid_fields["title"] = "x" * 501
        with self.assertRaises(ValueError) as context:
            validate_reference(self.ref_data)
        self.assertIn("cannot exceed 500 characters", str(context.exception))
