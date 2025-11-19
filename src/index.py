from app import app
from config import db

if __name__ == "__main__":

    # initialize db tables
    with app.app_context():
        db.create_all()

    # start the app
    app.run(port=5001, host="0.0.0.0", debug=True)
