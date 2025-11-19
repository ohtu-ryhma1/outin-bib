from flask import redirect, render_template, request, jsonify, flash
from config import app
from config import test_env

from services.reference_service import reference_service

from db_helper import reset_db

@app.route("/")
def index():
    references = reference_service.get_references()
    return render_template("index.html", references=references)

@app.route("/new_reference", methods=["GET", "POST"])
def new_reference():
    if request.method == "GET":
        return render_template("new_reference.html")

    if request.method == "POST":
        reference_type = request.form.get("type")
        reference_name = request.form.get("name")
        fields = {key: value for key, value in request.form.items() if key != "type"}

        try:
            reference_service.create_reference(reference_type, reference_name, fields)
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return redirect("/new_reference")

# testing routes
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return redirect("/")
