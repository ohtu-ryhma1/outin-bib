CREATE TABLE reference_types (
    reference_type_id SERIAL PRIMARY KEY,
    name              TEXT   NOT NULL,
);

CREATE TABLE field_types (
    field_type_id SERIAL PRIMARY KEY,
    name          TEXT NOT NULL
);

CREATE TABLE reference_field_type_associations (
    reference_type_id REFERENCES reference_types
    field_type_id     REFERENCES field_types
    PRIMARY KEY (reference_type_id, field_type_id)
);

CREATE TABLE references (
    reference_id SERIAL PRIMARY KEY,
    name         TEXT   NOT NULL
);

CREATE TABLE fields (
    field_id      SERIAL PRIMARY KEY,
    field_type_id INT    REFERENCES field_types(field_type_id),
    reference_id  INT    REFERENCES "references"(reference_id),
    value         TEXT   NOT NULL
);