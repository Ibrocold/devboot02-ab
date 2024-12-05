from app import create_app, db
from app.models import Contact

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)