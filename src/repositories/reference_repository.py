from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_reference_types():
    """Returns a set containing all available reference types with their ids"""

    sql = text(
        "SELECT reference_type_id AS id, name"
        "  FROM reference_types"
    )

    reference_types = db.session.execute(sql).fetchall()
    return set((rt.id, rt.name) for rt in reference_types)


def get_field_types():
    """Returns a set containing all available field types with their ids"""

    sql = text(
        "SELECT field_type_id AS id, name"
        "  FROM field_types"
    )

    field_types = db.session.execute(sql).fetchall()
    return set((ft.id, ft.name) for ft in field_types)


def get_references():
    """Returns a list of all references as Reference objects"""

    # get all references
    sql = text(
        "SELECT r.reference_id AS id, t.name AS type, r.name AS name"
        "  FROM references AS r"
        "  JOIN reference_types as t"
        "       ON r.reference_type_id = t.reference_type_id"
        " GROUP BY r.reference_id"
    )

    references = db.session.execute(sql).fetchall()

    # get all fields for all references
    sql = text(
        "SELECT t.name AS name, f.value AS value"
        "  FROM fields AS f"
        "  JOIN field_types AS t"
        "       ON f.field_type_id = t.field_type_id"
        " WHERE f.reference_id = :reference_id"
    )

    # create dictionary for each reference
    new_references = []
    for reference in references:
        # get fields for reference
        fields = db.session.execute(sql, {"reference_id": reference.id}).fetchall()
        fields = [(field.name, field.value) for field in fields]

        # construct the reference object
        new_reference = Reference(reference.type, reference.name, fields=fields)
        new_references.append(new_reference)

    return new_references


def create_reference(reference):
    """Add a new reference to the database"""

    # check if reference type is valid
    reference_type = next((t for t in get_reference_types() if t[1] == reference.type), None)
    if not reference_type:
        return None

    # add reference into database
    sql = text(
        "INSERT INTO references (reference_type_id, name)"
        "     VALUES (:reference_type_id, :name)"
        "  RETURNING reference_id"
    )

    params = {"reference_type_id": reference_type[0], "name": reference.name}
    new_reference_id = db.session.execute(sql, params).scalar()

    # add fields to database
    sql = text(
        "INSERT INTO fields (field_type_id, reference_id, value)"
        "     VALUES (:field_type_id, :reference_id, value)"
    )

    field_types = get_field_types()
    for field in reference.fields:
        # check if field type is valid
        field_type = next((t for t in field_types if t[1] == field.type), None)
        if not field_type:
            continue

        # add field to database
        params = {"field_type_id": field_type[0], "reference_id": new_reference_id,"value": field.value}
        db.session.execute(sql, params)

    db.session.commit()

    return new_reference_id


