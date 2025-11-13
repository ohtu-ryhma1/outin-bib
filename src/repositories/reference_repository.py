from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(text("SELECT id, title, author, year FROM refs"))
    refs = result.mappings().all() #jos luokka tehää sanakirjamuodos?
    return [Reference(ref["id"], ref["title"], ref["author"], ref["year"]) for ref in refs]


def create_reference(title, author, year):
    sql = text("INSERT INTO refs (title, author, year) VALUES (:title, :author, :year)")
    db.session.execute(sql, { "title": title, "author": author, "year": year })
    db.session.commit()