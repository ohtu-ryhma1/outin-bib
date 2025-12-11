from io import BytesIO

from flask import flash as _flash
from flask import (
    jsonify,
    redirect,
    render_template,
    request,
    send_file,
    url_for,
)


def flash(message, category="info", duration=10000):
    category = f"{category}|{duration}"
    _flash(message, category)


from sqlalchemy.exc import IntegrityError

from src.config import app
from src.services.bibtex_exporter import references_to_bibtex
from src.services.bibtex_import import import_bibtex_text
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
        key=key, types=ref_types, field_filters=field_filters
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
    ref_type = request.form.get("ref-type-select")
    ref_key = request.form.get("ref-key-input")
    fields = {
        key: value
        for key, value in request.form.items()
        if key not in ("ref-type-select", "ref-key-input", "field-select") and value
    }

    ref_data = {
        "type": ref_type,
        "key": ref_key,
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
    ref_type = request.form.get("ref-type-select")
    ref_key = request.form.get("ref-key-input")
    fields = {
        key: value
        for key, value in request.form.items()
        if key not in ("id", "ref-type-select", "ref-key-input", "field-select")
        and value
    }

    ref_data = {
        "type": ref_type,
        "key": ref_key,
        "fields": fields,
    }

    try:
        ref_service.update(ref_id, ref_data)
        flash("Reference updated succesfully")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("edit_reference", ref_id=ref_id))


@app.get("/import-export")
def show_import_export():
    refs = ref_service.get_all()
    bibtex_text = references_to_bibtex(refs)
    return render_template(
        "import-export.html", nav="import-export", bibtex_text=bibtex_text
    )


@app.post("/import/text")
def import_from_text():
    try:
        bibtex_text = request.form.get("import-textarea", "")
        if not bibtex_text.strip():
            flash("No BibTeX text provided", "error")
            return redirect(url_for("show_import_export"))

        success_count, errors = import_bibtex_text(bibtex_text)
        if success_count:
            flash(f"Successfully imported {success_count} reference(s)")

        for error in errors:
            flash(error, "error")

    except IntegrityError:
        flash("A reference with this key already exists.", "error")
    except Exception as e:
        flash(f"Unexpected error: {str(e)}", "error")

    return redirect(url_for("show_import_export"))


@app.post("/import/file")
def import_from_file():
    if "import-file-input" not in request.files:
        flash("No file provided", "error")
        return redirect(url_for("show_import_export"))

    file = request.files["import-file-input"]

    if file.filename == "":
        flash("No file selected", "error")
        return redirect(url_for("show_import_export"))

    try:
        bibtex_text = file.read().decode("utf-8")
    except UnicodeDecodeError:
        flash(
            "Could not read file. Please ensure it is a valid UTF-8 text file.", "error"
        )
        return redirect(url_for("show_import_export"))

    if not bibtex_text.strip():
        flash("File is empty", "error")
        return redirect(url_for("show_import_export"))

    success_count, errors = import_bibtex_text(bibtex_text)

    if success_count > 0:
        flash(f"Successfully imported {success_count} reference(s)")

    for error in errors:
        flash(error, "error")

    return redirect(url_for("show_import_export"))


@app.post("/export/file")
def export_references():
    refs = ref_service.get_all()
    bibtex_text = references_to_bibtex(refs)

    buffer = BytesIO(bibtex_text.encode("utf-8"))
    buffer.seek(0)
    return send_file(
        buffer,
        mimetype="application/x-bibtex",
        as_attachment=True,
        download_name="references.bib",
    )


if app.config["TEST_ENV"]:

    @app.post("/test/reset-db")
    def reset_db():
        if ref_service.delete_all():
            return jsonify("database reset successfully"), 200
        return jsonify("database reset unsuccessful"), 500

    @app.get("/test/flash")
    def test_flash():
        for _ in range(5):
            flash("This is a test flash message.")
            flash(
                "This is a veeeeeeeeeeeeeeeeeeeeeeeeeeery long test flash message.",
                "error",
            )
            flash("This is a test flash message.", "success")
        return redirect(url_for("index"))
