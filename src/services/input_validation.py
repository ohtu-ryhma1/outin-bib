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

    # If a required field contains '/', either one of the fields
    # satisfies the requirement
    conditional_pairs = {
        "author/editor": ("author", "editor"),
        "year/date": ("year", "date"),
    }

    for combined, (first, second) in conditional_pairs.items():
        if combined in required_fields:
            if first in ref_fields or second in ref_fields:
                required_fields = [f for f in required_fields if f != combined]

    missing_required = [
        name
        for name in required_fields
        if name not in ref_fields or not ref_fields[name].strip()
    ]

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
