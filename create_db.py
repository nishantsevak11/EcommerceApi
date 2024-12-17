import os
from app import create_app
from extensions import db
from models.product import Product

def create_database():
    # Delete the database file if it exists
    db_file = 'ecommerce.db'
    if os.path.exists(db_file):
        os.remove(db_file)
        print(f"Deleted existing database: {db_file}")

    app = create_app()
    with app.app_context():
        # Create all tables
        db.create_all()
        print("Database tables created successfully!")

if __name__ == '__main__':
    create_database()
