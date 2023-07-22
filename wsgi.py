"""Application entry point."""
from app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, ssl_context='adhoc')
