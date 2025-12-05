"""BibTeX import service for parsing and importing BibTeX entries."""

from sqlalchemy.exc import IntegrityError

from src.repositories.reference_repository import reference_repository
from src.services.bibtex_parser import parse_bibtex
from src.services.input_validation import validate_reference
from src.services.reference_service import reference_service


def normalize_field_name(field_name: str) -> str:
    """
    Normalize BibTeX field names to match the database schema.

    Args:
        field_name: The field name from BibTeX.

    Returns:
        Normalized field name.
    """
    # Map common BibTeX field names to our schema
    field_mapping = {
        "journal": "journaltitle",
        "year": "year/date",
        "date": "year/date",
    }
    return field_mapping.get(field_name.lower(), field_name.lower())


def import_bibtex_text(text: str) -> tuple:
    """
    Import BibTeX entries from text.

    Args:
        text: BibTeX formatted text.

    Returns:
        Tuple of (success_count, errors) where errors is a list of error messages.
    """
    try:
        entries = parse_bibtex(text)
    except ValueError as err:
        return 0, [f"Parse error: {str(err)}"]

    success_count = 0
    errors = []

    for entry in entries:
        try:
            # Normalize field names
            normalized_fields = {}
            for field_name, field_value in entry["fields"].items():
                normalized_name = normalize_field_name(field_name)
                normalized_fields[normalized_name] = field_value

            ref_data = {
                "type": entry["type"],
                "key": entry["key"],
                "fields": normalized_fields,
            }

            # If entry uses crossref, skip strict required-field validation
            # per BibLaTeX rules - entries with crossref inherit fields from parent
            if "crossref" in normalized_fields:
                # Skip validation and directly create the reference
                reference_repository.create(ref_data)
            else:
                # Normal validation and creation
                reference_service.create(ref_data)

            success_count += 1
        except ValueError as err:
            errors.append(f"Entry '{entry['key']}': {str(err)}")
        except IntegrityError:
            errors.append(
                f"Entry '{entry['key']}': Reference with this key already exists"
            )

    return success_count, errors
