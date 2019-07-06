from google.cloud import storage

from flask import Flask, request
from flask_injector import FlaskInjector

app = Flask(__name__)


@app.route("/")
def main(scp: storage.Client):
    print(scp)
    return "Welcome!"


def configure(binder):
    binder.bind(
        storage.Client,
        to=storage.Client(':memory:'),
        scope=request
    )

FlaskInjector(app=app, modules=[configure])

if __name__ == "__main__":
    app.run()
