from flask import Flask
from app import db


def init_db_command():
    db.create_all()
    print("Initialized the database.")


def init_app(app: Flask):
    app.cli.add_command(init_db_command, name='init-db')
