from bibtexparser import write_string
from bibtexparser.library import Library
from bibtexparser.model import Field, Entry

def references_to_bibtex(refs: list) -> str:
    lib = Library()

    for ref in refs:
        lib.add(Entry(ref.type, ref.key, [Field(f.type, f.value) for f in ref.fields]))

    return write_string(lib)
