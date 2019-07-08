from flask import Flask
from flask_injector import FlaskInjector

def storage():
    print('test')

app = Flask(__name__)

def configure(binder):
    binder.bind(
        storage,
        to=storage(':memory:'),
        scope=request
    )

FlaskInjector(app=app, modules=[configure])

def test_file_upload():
    print('test')