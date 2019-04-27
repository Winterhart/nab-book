
class DatabaseConfig():
    
    sql_lite_db_uri = ""

    def get_db_uri():
        return sql_lite_db_uri

    def setup_db_uri(app):
        app.config['SQLALCHEMY_DATABASE_URI'] = sql_lite_db_uri