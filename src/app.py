from flask import flash, redirect, render_template, request, url_for

from src.config import app
from src.services.reference_service import reference_service as ref_service
from src.services.reference_types import get_reference_fields, get_reference_types


@app.get("/")
def index():
    # get filters for template and service
    selected_filters = []
    template_selected_filters = []
    i = 0
    while True:
        field = request.args.get(f'filters[{i}][field]')
        op = request.args.get(f'filters[{i}][op]')
        value = request.args.get(f'filters[{i}][value]')
        if field is None and op is None and value is None:
            break
        if field or op or value:
            selected_filters.append(f"{field}:{op}:{value}")
            template_selected_filters.append({"field": field, "op": op, "value": value})
        i += 1
    # get types
    selected_types = request.args.getlist("types")
    # get name
    name = request.args.get("name")

    # get references with filters
    references = ref_service.get_all()

    # get all possible fields and types
    all_fields = ["title", "date", "year"] # need service function!
    all_types = sorted(list(get_reference_types()))
    
    return render_template(
        "index.html",
        references=references,
        all_fields=all_fields,
        selected_filters=template_selected_filters,
        all_types=all_types,
        selected_types=selected_types,
        selected_name = name
     )


@app.get("/new_reference")
def show_new_reference():
    ref_type = request.args.get("type")
    ref_type = ref_type if ref_type else "book"
    required, optional = get_reference_fields(ref_type)
    all_refs = sorted(list(get_reference_types()))

    return render_template(
        "new_reference.html",
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
