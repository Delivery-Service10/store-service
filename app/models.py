from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

db = SQLAlchemy()


def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    if not database_exists(engine.url):
        create_database(engine.url)
        db.metadata.create_all(engine)
        db.session.commit()
    return engine


class Store(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)

    def create(self, username):
        self.username = username
        return self
