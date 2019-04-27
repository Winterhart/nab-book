from flask import Flask
from datasource.database import db, db_url

# using a function to add more configuration to the application
def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = False

    # Setup database URI with SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    
    # Init db
    db.init_app(app)

    # Add Blueprint
    

    return app


# @app.route('/')
# def sayHi():
#     return "nab-book"

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
