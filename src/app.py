from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from config import app, test_env
from repositories.reference_repository import get_references, create_reference

@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)

@app.route("/new_reference")
def new():
    return render_template("new_reference.html")

@app.route("/create_reference", methods=["POST"])
def ref_creation():
    title = request.form.get("title")
    author = request.form.get("author")
    year = request.form.get("year")

    try:
        create_reference(title, author, year)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_reference")

@app.route("/create_refrence", methods=["GET", "POST"])
def refrence_creation():

    if request.method == "GET":
        return render_template("new_refrence.html")

    if request.method == "POST":
        return jsonify(request.form)

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })
