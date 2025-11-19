"""
input_validation.py

Functions to validate user input for reference creation.
Raises ValueError if input is invalid.
"""
from scripts.bibtex_types import types

def get_reference_fields(reference_type):
    """Return required and optional fields for a given BibTeX reference type."""
    if reference_type not in types:
        raise ValueError(f"Invalid reference type: {reference_type}")

    required_fields = types[reference_type]["required"]
    optional_fields = types[reference_type]["optional"]

    return required_fields, optional_fields

def validate_reference(reference_type, reference_name, fields):
    """
    Validate a new reference input

    Args:
        reference_type (str): Type of the BibTeX-reference
        reference_name (str): Unique identifier for the reference.
        fields (dict[str, str]): Dictionary of field_name and field_value.

    Raises:
        ValueError: If any validation rule fails.
    """
    if not reference_name.strip() or len(reference_name) > 100:
        raise ValueError("Reference name must be 1-100 characters long")

    required_fields, optional_fields = get_reference_fields(reference_type)

    missing_required = [name for name in required_fields if name not in fields or not fields[name].strip()]
    if missing_required:
        raise ValueError("Required fields missing: " + ", ".join(missing_required))

    unknown_fields = [name for name in fields if name not in required_fields and name not in optional_fields]
    if unknown_fields:
        raise ValueError("Unknown fields: " + ", ".join(unknown_fields))

    for name, value in fields.items():
        if value and len(value) > 500:
            raise ValueError(f"Field '{name}' cannot exceed 500 characters")
