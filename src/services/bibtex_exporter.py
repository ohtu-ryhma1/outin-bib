from bibtexparser import write_string
from bibtexparser.library import Library
from bibtexparser.model import Entry, Field


def references_to_bibtex(refs: list) -> str:
    if not refs:
        return ""

    lib = Library()

    for ref in refs:
        lib.add(Entry(ref.type, ref.key, [Field(f.type, f.value) for f in ref.fields]))

    raw_text = write_string(lib)
    bibtex_text = raw_text.replace("\t", "  ")

    while "\n\n\n" in bibtex_text:
        bibtex_text = bibtex_text.replace("\n\n\n", "\n\n")

    return bibtex_text
