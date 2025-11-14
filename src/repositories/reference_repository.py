from config import db
from sqlalchemy import text

from entities.reference import Reference

def get_references():
    result = db.session.execute(text("SELECT id, title, author, year FROM refs"))
    refs = result.fetchall() 
    return [Reference(entry_id=ref.id, title=ref.title, author=ref.author, year=ref.year) for ref in refs]


def create_reference(entry_id, title, author, year):
    sql = text("INSERT INTO refs (entry_id, title, author, year) VALUES (:entry_id, :title, :author, :year)")
    db.session.execute(sql, {"entry_id": entry_id, "title": title, "author": author, "year": year })
    db.session.commit()