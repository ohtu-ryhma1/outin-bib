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


def get_all_reference_fields() -> list:
    """
    Return a sorted list of BibTeX field names.
    """
    fields = set()

    for _, defs in types.items():
        for f in defs.get("required", []):
            fields.add(f)
        for f in defs.get("optional", []):
            fields.add(f)

    return sorted(fields)
