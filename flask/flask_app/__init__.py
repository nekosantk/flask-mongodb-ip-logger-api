from flask import Flask
from flask_mongoengine import MongoEngine
import os
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_cors import CORS

app = Flask(__name__, instance_relative_config=True)

app.config['MONGODB_SETTINGS'] = {
    'db':'db_name',
    'host': os.getenv("MONGO_SERVER_ADDRESS"),
    'port': int(os.getenv('MONGO_SERVER_PORT')),
    'username': os.getenv('MONGO_INITDB_ROOT_USERNAME'),
    'password': os.getenv('MONGO_INITDB_ROOT_PASSWORD')
}

app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

CORS(app)
cors = CORS(app, resource={
    r"/*":{
        "origins":"*"
    }
})

db = MongoEngine()
db.init_app(app)


def create_app():
    with app.app_context():
        from . import routes
        return app
