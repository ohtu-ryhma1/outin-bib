from src.scripts.bibtex_types import generic_fields, types


def get_reference_types() -> set:
    """Return all reference types in a set"""
    return set(types.keys())


def get_reference_fields(ref_type: str) -> tuple:
    """Return required and optional fields for a given BibTeX reference type.

    The optional fields include both type-specific optional fields and
    all generic biblatex fields, without duplicates. Required fields
    are never included in the optional list.
    """
    if ref_type not in types:
        raise ValueError(f"Invalid reference type: {ref_type}")

    required_fields = types[ref_type]["required"]
    type_optional = types[ref_type]["optional"]

    # Combine type-specific optional fields with generic fields
    required_set = set(required_fields)
    combined_optional = set(type_optional)
    combined_optional.update(generic_fields)

    # Remove any fields that are in required (avoid duplicates across lists)
    combined_optional -= required_set

    return required_fields, list(combined_optional)


def get_all_field_types() -> set:
    field_types = set()
    for ref in get_reference_types():
        required, optional = get_reference_fields(ref)
        field_types = field_types.union(set(required), set(optional))

    return field_types
