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

    def test_validate_reference_success(self):
        validate_reference("article", "ref1", self.valid_fields)

    def test_validate_reference_missing_required(self):
        fields = {
            "author": "Random Author",
            "title": "Example Article"
        }

        with self.assertRaises(ValueError) as context:
            validate_reference("article", "ref2", fields)
        self.assertIn("Required fields missing", str(context.exception))

    def test_validate_reference_unknown_field(self):
        fields = self.valid_fields.copy()
        fields["nonexistent"] = "unknown"

        with self.assertRaises(ValueError) as context:
            validate_reference("article", "ref3", fields)
        self.assertIn("Unknown fields", str(context.exception))

    def test_validate_reference_name_length(self):
        with self.assertRaises(ValueError) as context:
            validate_reference("article", "", self.valid_fields)
        self.assertIn("Reference name must be 1-100 characters long", str(context.exception))

        long_name = "x" * 101
        with self.assertRaises(ValueError) as context:
            validate_reference("article", long_name, self.valid_fields)
        self.assertIn("Reference name must be 1-100 characters long", str(context.exception))

    def test_validate_reference_field_too_long(self):
        fields = self.valid_fields.copy()
        fields["title"] = "x" * 501

        with self.assertRaises(ValueError) as context:
            validate_reference("article", "ref5", fields)
        self.assertIn("cannot exceed 500 characters", str(context.exception))
