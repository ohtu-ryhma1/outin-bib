from flask import redirect, render_template, request, jsonify, flash

from config import app, db
from config import test_env

from services.reference_service import reference_service as ref_service


@app.get("/")
def index():
    references = ref_service.get_all()
    return render_template("index.html", references=references)


@app.get("/new_reference")
def show_new_reference():
    return render_template("new_reference.html")


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

    ref_service.create(ref_data)
    return redirect("/")
