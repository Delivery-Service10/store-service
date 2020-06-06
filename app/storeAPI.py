from flask import Blueprint

store_api = Blueprint('store_api', __name__)


@store_api.route("/store")
def storeList():
    return 'Hello WorldAPI!'


# @app.route('/')
# def hello_world():
#     return 'Hello World!'
