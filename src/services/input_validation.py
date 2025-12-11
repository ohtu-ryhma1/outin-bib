"""Functions to validate user input for reference creation."""

from src.services.reference_types import get_reference_fields


def validate_reference(ref_data: dict):
    """
    Validate a new reference input

    Args:
        reference_type (str): Type of the BibTeX-reference
        reference_key (str): Unique identifier for the reference.
        fields (dict[str, str]): Dictionary of field_name and field_value.

    Raises:
        ValueError: If any validation rule fails.
    """
    ref_type = ref_data["type"]
    ref_key = ref_data["key"]
    ref_fields = ref_data["fields"]

    if not ref_key.strip() or len(ref_key) > 100:
        raise ValueError("Reference key must be 1-100 characters long")

    required_fields, optional_fields = get_reference_fields(ref_type)

    missing_required = [
        name
        for name in required_fields
        if name not in ref_fields or not ref_fields[name].strip()
    ]

    # If a required field contains '/', either one of the fields
    # satisfies the requirement
    if "year/date" in missing_required:
        if ("year" in ref_fields and ref_fields["year"].strip()) or (
            "date" in ref_fields and ref_fields["date"].strip()
        ):
            missing_required.remove("year/date")
            required_fields = [f for f in required_fields if f != "year/date"]

    if "author/editor" in missing_required:
        if ("author" in ref_fields and ref_fields["author"].strip()) or (
            "editor" in ref_fields and ref_fields["editor"].strip()
        ):
            missing_required.remove("author/editor")
            required_fields = [f for f in required_fields if f != "author/editor"]

    if missing_required:
        raise ValueError("Required fields missing: " + ", ".join(missing_required))

    unknown_fields = [
        name
        for name in ref_fields
        if name not in required_fields and name not in optional_fields
    ]

    if unknown_fields:
        raise ValueError("Unknown fields: " + ", ".join(unknown_fields))

    for name, value in ref_fields.items():
        if value and len(value) > 1500:
            raise ValueError(f"Field '{name}' cannot exceed 1500 characters")
