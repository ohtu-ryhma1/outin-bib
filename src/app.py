from flask import flash, jsonify, redirect, render_template, request, url_for

from src.config import app
from src.services.reference_service import reference_service as ref_service
from src.services.reference_types import (
    get_all_field_types,
    get_reference_fields,
    get_reference_types,
)


@app.get("/")
def index():
    key = request.args.get("ref-key")
    ref_types = request.args.getlist("ref-type")
    filter_field_types = request.args.getlist("field-type")
    filter_field_values = request.args.getlist("field-value")
    field_filters = list(zip(filter_field_types, filter_field_values))

    refs = ref_service.get_all_meta(
        name=key, types=ref_types, field_filters=field_filters
    )

    all_ref_types = sorted(get_reference_types())
    all_field_types = sorted(get_all_field_types())

    return render_template(
        "index.html",
        nav="index",
        refs=refs,
        key=key,
        ref_types=ref_types,
        field_filters=field_filters,
        all_ref_types=all_ref_types,
        all_field_types=all_field_types,
    )


@app.get("/new-reference")
def show_new_reference():
    ref_type = request.args.get("type") or "book"
    required, optional = get_reference_fields(ref_type)
    all_refs = sorted(list(get_reference_types()))

    return render_template(
        "new-reference.html",
        nav="new",
        all_refs=all_refs,
        ref_type=ref_type,
        required=required,
        optional=optional,
    )


@app.post("/new-reference")
def new_reference():
    ref_type = request.form.get("ref-type-input")
    ref_key = request.form.get("ref-key-input")
    fields = {
        key: value
        for key, value in request.form.items()
        if key not in ("ref-type-input", "ref-key-input", "field-select") and value
    }

    ref_data = {
        "type": ref_type,
        "name": ref_key,
        "fields": fields,
    }

    try:
        ref_service.create(ref_data)
        flash("New reference created!")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("show_new_reference", type=ref_type))


@app.get("/edit-reference")
def show_edit_reference():
    ref_id = request.args.get("id")
    ref = ref_service.get(ref_id=ref_id)

    required, optional = get_reference_fields(ref.type)
    ref_types = sorted(list(get_reference_types()))

    ref.optional = set(field.type for field in ref.fields if field.type in optional)

    return render_template(
        "edit-reference.html",
        nav="index",
        ref=ref,
        ref_types=ref_types,
        required=required,
        optional=optional,
    )


@app.post("/edit-reference")
def edit_reference():
    ref_id = request.args.get("id")
    ref_type = request.form.get("ref-type-input")
    ref_key = request.form.get("ref-key-input")
    fields = {
        key: value
        for key, value in request.form.items()
        if key not in ("id", "ref-type-input", "ref-key-input", "field-select")
        and value
    }

    ref_data = {
        "type": ref_type,
        "name": ref_key,
        "fields": fields,
    }

    try:
        ref_service.update(ref_id, ref_data)
        flash("Reference updated succesfully")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("edit_reference", ref_id=ref_id))


if app.config["TEST_ENV"]:

    @app.post("/test/reset-db")
    def reset_db():
        if ref_service.delete_all():
            return jsonify("database reset succesfully"), 200
        return jsonify("database reset unsuccesful"), 500
