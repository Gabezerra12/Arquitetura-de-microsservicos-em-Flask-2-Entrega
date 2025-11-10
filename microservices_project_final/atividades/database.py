from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
def init_db(app, sqlite_file):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{sqlite_file}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    with app.app_context():
        db.create_all()
