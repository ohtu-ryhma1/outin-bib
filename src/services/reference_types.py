from src.scripts.bibtex_types import types


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


def get_all_field_types() -> set:
    field_types = set()
    for ref in get_reference_types():
        required, optional = get_reference_fields(ref)
        field_types = field_types.union(set(required), set(optional))

    return field_types
