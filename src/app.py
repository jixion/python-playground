import sqlite3

from flask import Flask, request
from flask_injector import FlaskInjector

app = Flask(__name__)


@app.route("/")
def main(db: sqlite3.Connection):
    print(db)
    return "Welcome!"


def configure(binder):
    binder.bind(
        sqlite3.Connection,
        to=sqlite3.Connection(':memory:'),
        scope=request
    )

FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run()
