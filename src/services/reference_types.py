from scripts.bibtex_types import types


def get_reference_types() -> set:
    """Return all reference types in a set"""
    return set(types.keys())


def get_reference_fields(ref_type: str) -> tuple:
    """Return required and optional fields for a given BibTeX reference type."""
    if ref_type not in types:
        raise ValueError(f"Invalid reference type: {ref_type}")

    required_fields = types[ref_type]["required"]
    optional_fields = types[ref_type]["optional"]

    return required_fields, optional_fields
