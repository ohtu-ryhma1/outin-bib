"""Class to validate reference data"""

from src.services.reference_types import get_reference_fields


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
            self._check_missing_required,
            self._check_unknown_fields,
            self._check_field_lengths,
        ]

    def validate(self) -> None:
        """Run all validation checks. Raise ValueError on failure."""
        for check in self._checks:
            check()

    def _check_key(self) -> None:
        ref_key = self.ref_key
        if not ref_key.strip() or len(ref_key) > self.key_max_length:
            raise ValueError(
                f"Reference key must be 1-{self.key_max_length} characters long"
            )

    def _check_missing_required(self) -> None:
        ref_fields = self.ref_fields
        missing_required = [
            name
            for name in self.required_fields
            if name not in ref_fields or not ref_fields[name].strip()
        ]

        if "year/date" in missing_required:
            if ("year" in ref_fields and ref_fields["year"].strip()) or (
                "date" in ref_fields and ref_fields["date"].strip()
            ):
                missing_required.remove("year/date")
                self.required_fields = [
                    f for f in self.required_fields if f != "year/date"
                ]

        if "author/editor" in missing_required:
            if ("author" in ref_fields and ref_fields["author"].strip()) or (
                "editor" in ref_fields and ref_fields["editor"].strip()
            ):
                missing_required.remove("author/editor")
                self.required_fields = [
                    f for f in self.required_fields if f != "author/editor"
                ]

        if missing_required:
            raise ValueError("Required fields missing: " + ", ".join(missing_required))

    def _check_unknown_fields(self) -> None:
        unknown_fields = [
            name
            for name in self.ref_fields
            if name not in self.required_fields and name not in self.optional_fields
        ]

        if unknown_fields:
            raise ValueError("Unknown fields: " + ", ".join(unknown_fields))

    def _check_field_lengths(self) -> None:
        for name, value in self.ref_fields.items():
            if value and len(value) > self.max_field_length:
                raise ValueError(
                    f"Field '{name}' cannot exceed {self.max_field_length} characters"
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
