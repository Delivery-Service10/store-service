from flask import Flask
from storeAPI import store_api
import models
import os
from mysql import connector

app = Flask(__name__)



db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASS')
app.config['SECRET_KEY'] = 'ThisIsSecretKey'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + db_user + ':' + db_pass + '@localhost/store_test_db?auth_plugin=mysql_native_password'


models.init_app(app)
models.create_tables(app)
app.register_blueprint(store_api)


@app.route("/")
def hello():
    return "Welcome to the store_service_api"


if __name__ == '__main__':
    app.run(debug=True)
