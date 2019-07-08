from google.cloud import storage

from flask import Flask, request
from flask_injector import FlaskInjector

app = Flask(__name__)


@app.route("/")
def main(scp: storage.Client):
    print(scp)
    bucket = scp.bucket('br549')
    blob = bucket.blob('requirements.txt')
    blob.upload_from_file(open('requirements.txt', '+r'))
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
