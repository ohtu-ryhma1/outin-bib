from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

from dotenv import load_dotenv
from os import getenv

class Base(DeclarativeBase):
    pass

# load environment variables
load_dotenv()
test_env = getenv("TEST_ENV") == "true"
print(f"Test environment: {test_env}")

# create app instance
app = Flask(__name__)
app.secret_key = getenv("SECRET_KEY")

# use in-memory database if test_env is true
DB_URL = getenv("DEV_DATABASE_URL") if test_env else getenv("DATABASE_URL")
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL

# initialize database instance and connect it to the app instance
db = SQLAlchemy(model_class=Base)
db.init_app(app)