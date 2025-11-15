from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
from repositories.reference_repository import get_references, create_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/new_reference", methods=["GET", "POST"])
def new_ref():
    if request.method == "GET":
        return render_template("new_reference.html")

    if request.method == "POST":
        fields = {key: value for key, value in request.form.items() if key != "Type"}
        type_name = request.form.get("Type")

        try:
            create_reference(type_name, fields)
            return redirect("/")
        except Exception as error:
            flash(str(error))
            return redirect("/new_reference")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
