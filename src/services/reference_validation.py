"""Class to validate reference data"""

from enum import StrEnum, auto

from src.services.reference_types import get_reference_fields


class ErrorCode(StrEnum):
    """Enumeration of error codes for validation errors"""

    KEY_LENGTH_INVALID = auto()
    FIELD_LENGTH_INVALID = auto()
    REQUIRED_FIELD_MISSING = auto()
    UNKNOWN_FIELD_PRESENT = auto()


class ValidationException(Exception):
    """Exception for validation errors. Supports error codes."""

    def __init__(self, code: ErrorCode, message: str):
        super().__init__(message)
        self.code = code


class ReferenceValidator:
    """Class to validate reference data"""

    def __init__(
        self, ref_data: dict, max_field_length: int = 1500, key_max_length: int = 100
    ):
        self.ref_data = ref_data
        self.ref_type = ref_data["type"]
        self.ref_key = ref_data["key"]
        self.ref_fields = ref_data["fields"]
        self.max_field_length = max_field_length
        self.key_max_length = key_max_length

        required_fields, optional_fields = get_reference_fields(self.ref_type)
        self.required_fields = list(required_fields)
        self.optional_fields = list(optional_fields)

        self._checks = [
            self._check_key,
            self._check_required_fields,
            self._check_unknown_fields,
            self._check_field_lengths,
        ]

    def validate(self) -> None:
        """Run all validation checks. Raise ValidationException with appropriate error code on failure."""
        for check in self._checks:
            check()

    def _check_key(self) -> None:
        ref_key = self.ref_key
        if not ref_key.strip() or len(ref_key) > self.key_max_length:
            raise ValidationException(
                ErrorCode.KEY_LENGTH_INVALID,
                f"Reference key must be 1-{self.key_max_length} characters long",
            )

    def _check_required_fields(self) -> None:
        ref_fields = self.ref_fields
        missing_required = [
            name
            for name in self.required_fields
            if name not in ref_fields or not ref_fields[name].strip()
        ]

        # handle alternative required fields (e.g., "author/editor")
        for field_type in missing_required:
            if "/" in field_type:
                parts = field_type.split("/")
                if any(
                    part in ref_fields and ref_fields[part].strip() for part in parts
                ):
                    missing_required.remove(field_type)

        if missing_required:
            raise ValidationException(
                ErrorCode.REQUIRED_FIELD_MISSING,
                "Required fields missing: " + ", ".join(missing_required),
            )

    def _check_unknown_fields(self) -> None:
        unknown_fields = [
            name
            for name in self.ref_fields
            if name not in self.required_fields and name not in self.optional_fields
        ]

        if unknown_fields:
            raise ValidationException(
                ErrorCode.UNKNOWN_FIELD_PRESENT,
                "Unknown fields: " + ", ".join(unknown_fields),
            )

    def _check_field_lengths(self) -> None:
        for name, value in self.ref_fields.items():
            if value and len(value) > self.max_field_length:
                raise ValidationException(
                    ErrorCode.FIELD_LENGTH_INVALID,
                    f"Field '{name}' cannot exceed {self.max_field_length} characters",
                )


def validate_reference(
    ref_data: dict,
    max_field_length: int = 1500,
    key_max_length: int = 100,
) -> None:
    ReferenceValidator(
        ref_data,
        max_field_length=max_field_length,
        key_max_length=key_max_length,
    ).validate()
