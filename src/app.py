from flask import redirect, render_template, request, jsonify, flash, url_for

from config import app, db

from services.reference_service import reference_service as ref_service
from services.reference_types import get_reference_types, get_reference_fields


@app.get("/")
def index():
    references = ref_service.get_all()
    return render_template("index.html", references=references)
        
@app.get("/new_reference")
def show_new_reference():
    ref_type = request.args.get("type") 
    ref_type = ref_type if ref_type else "book"
    required, optional = get_reference_fields(ref_type)
    all_refs = sorted(list(get_reference_types())) 
    return render_template("new_reference.html", all_refs = all_refs, ref_type = ref_type, required = required, optional = optional)

@app.post("/new_reference")
def create_new_reference():
    ref_type = request.form.get("type")
    ref_name = request.form.get("name")
    fields = {key: value for key, value in request.form.items() if key not in ("type", "name")}
    ref_data = {
        "type": ref_type,
        "name": ref_name,
        "fields": fields
    }

    try:
        ref_service.create(ref_data)
        flash("New reference created!")
        return redirect("/")

    except ValueError as error:
        flash(str(error), "error")
        return redirect(url_for("show_new_reference", type=ref_type))

    except Exception:
        flash("Unexpected error!")
        return redirect(url_for("show_new_reference", type=ref_type))
