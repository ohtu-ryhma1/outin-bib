"""BibTeX export functionality for converting references to BibTeX format."""


def reference_to_bibtex(ref) -> str:
    """
    Convert a Reference object to BibTeX format.

    Args:
        ref: Reference object with type, name, and fields attributes.

    Returns:
        BibTeX formatted string for the reference.
    """
    lines = [f"@{ref.type}{{{ref.name},"]

    for field in ref.fields:
        value = field.value
        # Escape special characters and wrap in braces
        lines.append(f"  {field.type} = {{{value}}},")

    lines.append("}")
    return "\n".join(lines)


def references_to_bibtex(refs: list) -> str:
    """
    Convert a list of Reference objects to BibTeX format.

    Args:
        refs: List of Reference objects.

    Returns:
        BibTeX formatted string containing all references.
    """
    entries = []
    for ref in refs:
        entries.append(reference_to_bibtex(ref))
    return "\n\n".join(entries)
