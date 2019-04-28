from flask import Flask
from datasource.database import db, db_url
from views import general
from views.contact import ContactView
from datasource.database_init import init_db

# using a function to add more configuration to the application
def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = False

    # Setup database URI with SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    # Init db
    db.init_app(app)
    init_db()
    # Prevent sorting JSON
    app.config["JSON_SORT_KEYS"] = False
    
    # Add Blueprint
    app.register_blueprint(general.main)
    app.register_blueprint(ContactView.contact)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
