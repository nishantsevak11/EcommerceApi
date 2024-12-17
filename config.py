import os

class Config:
    # Get the absolute path to the directory containing this file
    basedir = os.path.abspath(os.path.dirname(__file__))
    
    # SQLite database file will be created in the same directory as this file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'ecommerce.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
