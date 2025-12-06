from bibtexparser import dumps
from bibtexparser.bibdatabase import BibDatabase
from bibtexparser.bwriter import BibTexWriter

def to_dict(ref) -> str:
    ref_dict = {
        "ENTRYTYPE": ref.type,
        "ID" : ref.key,
    }
    for field in ref.fields:
        ref_dict[field.type] = field.value

    return ref_dict


def references_to_bibtex(refs: list) -> str:
    db = BibDatabase()
    db.entries = []
    for ref in refs:
        db.entries.append(to_dict(ref))

    writer = BibTexWriter()
    writer.contents = ['entries']
    writer.indent = '  '
    return dumps(db, writer)
