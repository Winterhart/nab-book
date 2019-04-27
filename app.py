from flask import Flask
from settings import DatabaseConfig
from datasource.database import db

# using a function to add more configuration to the application
def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = False

    # Setup database URI with SQLite
    configurator  = DatabaseConfig()
    configurator.setup_db_uri(app)
    # Init db
    db.init_app()

    # Add Blueprint
    


@app.route('/')
def sayHi():
    return "nab-book"

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0")
