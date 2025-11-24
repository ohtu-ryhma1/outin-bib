from flask import flash, redirect, render_template, request, url_for

from src.config import app
from src.services.reference_service import reference_service as ref_service
from src.services.reference_types import get_reference_fields, get_reference_types


@app.get("/")
def index():
    refs = ref_service.get_all()
    return render_template(
        "index.html",
        nav="index",
        refs=refs,
    )


@app.get("/new_reference")
def show_new_reference():
    ref_type = request.args.get("type")
    ref_type = ref_type if ref_type else "book"
    required, optional = get_reference_fields(ref_type)
    all_refs = sorted(list(get_reference_types()))

    return render_template(
        "new_reference.html",
        nav="new",
        all_refs=all_refs,
        ref_type=ref_type,
        required=required,
        optional=optional,
    )


@app.post("/new_reference")
def new_reference():
    ref_type = request.form.get("type")
    ref_name = request.form.get("name")
    fields = {
        key: value for key, value in request.form.items() if key not in ("type", "name")
    }

    ref_data = {
        "type": ref_type,
        "name": ref_name,
        "fields": fields,
    }

    try:
        ref_service.create(ref_data)
        flash("New reference created!")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("show_new_reference", type=ref_type))


@app.get("/edit_reference")
def show_edit_reference():
    ref_id = request.args.get("id")
    ref = ref_service.get(ref_id=ref_id)

    required, optional = get_reference_fields(ref.type)
    ref_types = sorted(list(get_reference_types()))

    ref.optional = set(field.type for field in ref.fields if field.type in optional)

    return render_template(
        "edit_reference.html",
        nav="index",
        ref=ref,
        ref_types=ref_types,
        required=required,
        optional=optional,
    )


@app.post("/edit_reference")
def edit_reference():
    ref_id = request.form.get("id")
    ref_type = request.form.get("type")
    ref_name = request.form.get("name")
    fields = {
        key: value
        for key, value in request.form.items()
        if key not in ("id", "type", "name")
    }

    ref_data = {
        "type": ref_type,
        "name": ref_name,
        "fields": fields,
    }

    try:
        ref_service.update(ref_id, ref_data)
        flash("Reference updated succesfully")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("edit_reference", ref_id=ref_id, type=ref_type))
